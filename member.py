import pyqrcode


class Member:
    def __init__(self, member_id, name, email, phone_number, participation_state):
        self.id = member_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.participation_state = participation_state

    def __str__(self):
        return f"Member id: {self.id}\n" \
               f"Name: {self.name}\n" \
               f"Email: {self.email}\n" \
               f"Phone Number: {self.phone_number}\n" \
               f"Participation State: {self.participation_state}"

    def getMemberQRCode(self):
        member_date = self.__str__()
        image = pyqrcode.create(member_date)
        return image


member_attributes = ['ID', 'Name', 'Email', 'Phone Number', 'Participation As', 'QRCODE']
