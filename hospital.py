class Patient(object):
    pcount = 1
    def __init__(self, name, allergic):
        self.name = name
        self.allergic = allergic
        self.id = Patient.pcount
        self.bed_number = None
        Patient.pcount += 1

class Hospital(object):
    def __init__ (self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.beds = self.start_beds()

    def start_beds(self):
        beds = []
        for i in range(1, self.capacity):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds
    def admit(self, patient):
        if len(self.patients) <= self.capacity:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    break
            print "Patient #{} admitted to bed #{}".format(patient.id, patient.bed_num)
        else:
            "Hospital is at full capacity"
    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                # free up bed
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break

                self.patients.remove(patient)
                return "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_num)
        return "Patient not found"

## Doing stuff
myhospital = Hospital("Super Hospital", 120)
bill = Patient("Bill", "Nothing")
myhospital.admit(bill)