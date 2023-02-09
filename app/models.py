from dataclasses import dataclass


class Serializable:
    """
    Serializable class used to map constructor keywords to new instance attributes
    """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if " " in key:
                key = key.replace(" ", "")
            setattr(self, key, value)


@dataclass
class Experience:
    """
    Model that maps over a single candidate's experience
    """
    employer: str
    contract_type: str
    start_date: str
    end_date: str
    description: str


@dataclass
class Education:
    """
    Model that maps over a single Education entry of a candidate
    """
    institution: str
    level: str
    field: str
    diploma: str


class CV(Serializable):
    """
    Model the contains the necessary info of a candidate's CV
    """
    name: str
    address: str
    experience: list[Experience]
    education: list[Education]
