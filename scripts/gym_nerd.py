import pandas as pd
from enum import Enum
from nicegui import ui, events

groupings = {"Chest":["Clavicular", "Sternal", "Abdominal"],
             "Arm":["Bicep","Tripep","Forearm"],
             "Shoulder":["Anterior","Lateral","Posterior"],
             "Core":["Abdominis","Oblique","Serratus"],
             "Legs":["Quadricep","Hamstring","Glute","Calf"],
             "Back":["Trapezius","Latissimus","Lower"]
}

class Tier1FilterMode(Enum):
    DISABLED = 1
    PARTIAL_ENABLE = 2
    ENABLED = 3
    

class FilterTracker():
    def __init__(self):
        self.tier1 = {key:False for key in groupings.keys()}
        self.tier2 = {key:False for item in groupings.values() for key in item}
    def filter_flip_flop(self, keyword):
        if keyword in self.tier1.keys():
            self.tier1[keyword] = not(self.tier1[keyword])
        if keyword in self.tier2.keys():
            self.tier2[keyword] = not(self.tier2[keyword])
    def get_tier1_filters(self):
        retval = []
        for key, value in self.tier1:
            if value == True:
                retval.append(key)
        return retval
    def get_tier2_filters(self):
        retval = []
        for key, value in self.tier2:
            if value == True:
                retval.append(key)
        return retval
class GymNerd():
    def __init__(self):
        self.df = pd.read_csv("data/db.csv", header=0, quotechar="\"")
        self.columns = self.df.columns
        self.columns_no_uid = self.df.columns[0:5]
        self.clean()
        self.test_value = False
        self.filtered_df = self.df

        self.filterer = FilterTracker()

    def clean(self):
        for index, row in self.df.iterrows():
            # Exercise
            self.df.at[index,"Exercise"] = str.title(row["Exercise"])
            # Groups
            self.df.at[index,"Groups"] = self.clean_list_string(row["Groups"])
            # Exercises
            self.df.at[index,"Muscles"] = self.clean_list_string(row["Muscles"])
            # Machine
            self.df.at[index,"Machine"] = str.title(row["Machine"])
    def clean_list_string(self, target):
        if(type(target) != type([])):
            new_list = []
            target_list = target.split()
            for i in range(0, len(target_list)):
                result = target_list[i].strip()
                result = result.replace(",","")
                result = str.title(result)
                new_list.append(result)
            return ", ".join(new_list)
        else:
            return target
    def save(self):
        self.df.to_csv("data/db2.csv",index=False)

    def filter(self, keyword):

        self.filterer.filter_flip_flop(keyword)

        keep = []
        
        for index, row in self.df.iterrows():
            if thing in row["Groups"]:
                keep.append(row)
        self.filtered_df = pd.DataFrame(keep)

#        print(self.df["Chest, Shoulder" == self.df["Groups"]])

nerd = GymNerd()
nerd.clean()
nerd.save()