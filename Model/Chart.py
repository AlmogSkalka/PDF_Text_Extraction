from datetime import datetime


class Chart:
    name: str
    dob: datetime
    has_valid_ekg: bool

    def __init__(self, patient_name: str, patient_dob: datetime, has_valid_ekg: bool):
        self.name = patient_name
        self.dob = patient_dob
        self.has_valid_ekg = has_valid_ekg

    @property
    def age(self) -> float:
        if self.dob is not None:
            today = datetime.today()
            birthdate = self.dob
            age = (
                    today.year
                    - birthdate.year
                    - ((today.month, today.day) < (birthdate.month, birthdate.day))
            )
            return age
