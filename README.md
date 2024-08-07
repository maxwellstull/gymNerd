# gymNerd
A script allowing for searching of a self-curated exercise database based on muscle group, individual muscles, workout machines/tools, with the end goal of not getting bored doing the same 4 workouts at the gym every week.

## Setup
This setup assumes you have Python installed. I am using Python3.10.10.
1. Clone this repository
```bash
git clone https://github.com/maxwellstull/gymNerd.git
```
2. Navigate to repository
```bash
cd path/to/gymNerd/
```
3. Create a virtual environment
```bash
python3 -m venv venv
```
4. Activate virtual environment
```bash
#Windows
./venv/Scripts/activate

#Linux/Mac (untested, but trivial)
source venv/bin/activate
```
5. Install requirements
```bash
pip install -r requirements.txt
```
## Info
### Disclaimers
1. All of this should be taken with a grain of salt - I am a nerd who has been going to the gym regularly for about 8 months after only doing cardio for most of my life, most of the information for this comes from what I already know or the front page of google. 
2. Don't hurt yourself. Going from being lethargic to going to the gym 8 times a week is a great way to end up seeing a physical therapist.
3. Motivation shows up when you do.

### Muscle Groupings
For filtering individual exercises, the 

| Group | Sub-Groups | Notes |
|-------|---------|------|
| Chest  | Clavicular | *Upper chest*
| | Sternal | *Middle chest*
| | Abdominal | *Lower chest*
| Arm | Bicep | 
| | Tricep | 
| | Forearm |
| Shoulder | Anteroir | *Front of shoulder* |
| | Lateral | *Middle of shoulder* |
| | Posterior | *Rear of shoulder* |
| Core | Abdominis |  
| | Oblique | 
| | Serratus | *not technically in the area people think about when they think core, but I feel like it belongs here*
| Legs | Quadricep |  
| | Hamstring | 
| | Glute | 
| | Calf |
| Back | Trapezius | *Upper back*
| | Latissimus | *Middle back*
| | "Lower" | *Lower back doesn't have a particularly notable muscle*



# Todo
- [ ] Create search and filter script
- [ ] Create script that updates database
- [ ] Create database
- [ ] Create niceGUI
- [ ] Publish to online (??)






# Various Sources
[BodyBuilding.com](https://www.bodybuilding.com/exercises)