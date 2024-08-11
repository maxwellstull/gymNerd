import pandas as pd
from nicegui import ui, events
from gym_nerd import GymNerd


nerd = GymNerd()
def update_table():
    table.rows = nerd.filtered_df.to_dict("records")
    print("updated!")

with ui.row():
    with ui.column():
        with ui.row():
            main1 = "Chest"
            sub1A = "Clavicular"
            sub1B = "Sternal"
            sub1C = "Abdominal"

            m1 = ui.checkbox(main1)
            m1.on_value_change(lambda: [nerd.filter(main1), update_table()])
            subA1 = ui.checkbox(sub1A)
            subA1.bind_enabled_from(m1, "value")
            subA1.bind_value_from(m1, "value", backward=lambda x: x & False)
            subA1.on_value_change(lambda: [nerd.filter(sub1A), update_table()])
            subB1 = ui.checkbox(sub1B)
            subB1.bind_enabled_from(m1, "value")
            subB1.bind_value_from(m1, "value", backward=lambda x: x & False)
            subB1.on_value_change(lambda: [nerd.filter(sub1B), update_table()])
            subC1 = ui.checkbox(sub1C)
            subC1.bind_enabled_from(m1, "value")
            subC1.bind_value_from(m1, "value", backward=lambda x: x & False)
            subC1.on_value_change(lambda: [nerd.filter(sub1C), update_table()])
        with ui.row():
            main2 = "Arm"
            sub2A = "Bicep"
            sub2B = "Tricep"
            sub2C = "Forearm"

            m2 = ui.checkbox(main2)
            m2.on_value_change(lambda: [nerd.filter(main2), update_table()])
            subA2 = ui.checkbox(sub2A)
            subA2.bind_enabled_from(m2, "value")
            subA2.bind_value_from(m2, "value", backward=lambda x: x & False)
            subA2.on_value_change(lambda: [nerd.filter(sub2A), update_table()])
            subB2 = ui.checkbox(sub2B)
            subB2.bind_enabled_from(m2, "value")
            subB2.bind_value_from(m2, "value", backward=lambda x: x & False)
            subB2.on_value_change(lambda: [nerd.filter(sub2B), update_table()])
            subC2 = ui.checkbox(sub2C)
            subC2.bind_enabled_from(m2, "value")
            subC2.bind_value_from(m2, "value", backward=lambda x: x & False)
            subC2.on_value_change(lambda: [nerd.filter(sub2C), update_table()])
    with ui.column():
        with ui.row():
            main3 = "Shoulder"
            sub3A = "Anterior"
            sub3B = "Lateral"
            sub3C = "Posterior"

            m3 = ui.checkbox(main3)
            m3.on_value_change(lambda: [nerd.filter(main3), update_table()])
            subA3 = ui.checkbox(sub3A)
            subA3.bind_enabled_from(m3, "value")
            subA3.bind_value_from(m3, "value", backward=lambda x: x & False)
            subA3.on_value_change(lambda: [nerd.filter(sub3A), update_table()])
            subB3 = ui.checkbox(sub3B)
            subB3.bind_enabled_from(m3, "value")
            subB3.bind_value_from(m3, "value", backward=lambda x: x & False)
            subB3.on_value_change(lambda: [nerd.filter(sub3B), update_table()])
            subC3 = ui.checkbox(sub3C)
            subC3.bind_enabled_from(m3, "value")
            subC3.bind_value_from(m3, "value", backward=lambda x: x & False)
            subC3.on_value_change(lambda: [nerd.filter(sub3C), update_table()])
        with ui.row():
            main4 = "Core"
            sub4A = "Abdominis"
            sub4B = "Oblique"
            sub4C = "Serratus"

            m4 = ui.checkbox(main4)
            m4.on_value_change(lambda: [nerd.filter(main4), update_table()])
            subA4 = ui.checkbox(sub4A)
            subA4.bind_enabled_from(m4, "value")
            subA4.bind_value_from(m4, "value", backward=lambda x: x & False)
            subA4.on_value_change(lambda: [nerd.filter(sub4A), update_table()])
            subB4 = ui.checkbox(sub4B)
            subB4.bind_enabled_from(m4, "value")
            subB4.bind_value_from(m4, "value", backward=lambda x: x & False)
            subB4.on_value_change(lambda: [nerd.filter(sub4B), update_table()])
            subC4 = ui.checkbox(sub4C)
            subC4.bind_enabled_from(m4, "value")
            subC4.bind_value_from(m4, "value", backward=lambda x: x & False)
            subC4.on_value_change(lambda: [nerd.filter(sub4C), update_table()])


def save():
    df = pd.DataFrame(table.rows)
    nerd.df = df
    nerd.save()
def add_row():
    table.add_rows({"Exercise":"","Groups":"","Muscles":"","Machine":"","Description":"","uid":max((dx['uid'] for dx in table.rows), default=-1) + 1})
def rename(e : events.GenericEventArguments):
    for row in table.rows:
        if row['uid'] == e.args['uid']:
            row.update(e.args)
    table.update()

columns=[{"name":col,"label":col,"field":col} for col in nerd.columns_no_uid]

table = ui.table(columns=columns, rows=nerd.df.to_dict("records"))
table.add_slot('body', r'''
    <q-tr :props="props">
        <q-td key="Exercise" :props="props">
            {{ props.row.Exercise }}
            <q-popup-edit v-model="props.row.Exercise" v-slot="scope"
                @update:model-value="() => $parent.$emit('rename', props.row)"
            >
                <q-input v-model="scope.value" dense autofocus @keyup.enter="scope.set" />
            </q-popup-edit>
        </q-td>
        </q-td>
               <q-td key="Groups" :props="props">
            {{ props.row.Groups }}
            <q-popup-edit v-model="props.row.Groups" v-slot="scope"
                @update:model-value="() => $parent.$emit('rename', props.row)"
            >
                <q-input v-model="scope.value" dense autofocus @keyup.enter="scope.set" />
            </q-popup-edit>
        </q-td>

        </q-td>
               <q-td key="Muscles" :props="props">
            {{ props.row.Muscles }}
            <q-popup-edit v-model="props.row.Muscles" v-slot="scope"
                @update:model-value="() => $parent.$emit('rename', props.row)"
            >
                <q-input v-model="scope.value" dense autofocus @keyup.enter="scope.set" />
            </q-popup-edit>
        </q-td>
               <q-td key="Machine" :props="props">
            {{ props.row.Machine }}
            <q-popup-edit v-model="props.row.Machine" v-slot="scope"
                @update:model-value="() => $parent.$emit('rename', props.row)"
            >
                <q-input v-model="scope.value" dense autofocus @keyup.enter="scope.set" />
            </q-popup-edit>
        </q-td>
               <q-td key="Description" :props="props">
            {{ props.row.Description }}
            <q-popup-edit v-model="props.row.Description" v-slot="scope"
                @update:model-value="() => $parent.$emit('rename', props.row)"
            >
                <q-input v-model="scope.value" dense autofocus @keyup.enter="scope.set" />
            </q-popup-edit>
        </q-td>
    </q-tr>
''')

ui.button('add row', on_click=add_row)
ui.button('save', on_click=save)

table.on('rename',rename)



ui.run()