

class Group():
    def __init__(self, name, password, id) -> None:
        self.id = id
        self.name = name
        self.password = password

    # in case we want to save it into mongodb
    # def save(self, db):
    #     if '_id' not in self:
    #         db.groups.insert_one(self)
    #     else:
    #         db.groups.update_one({'_id': self['_id']}, self)


    @staticmethod
    def login_group(group_name, password):
        if group_name in group_by_name and group_by_name[group_name].password == password:
            return group_by_name[group_name]
        return None
        
    def load_group(group_id):
        if group_id in group_by_id:
            return group_by_id[group_id]
        return None
        

# security note: group_id should not be guessable
group_list = [
    Group("testGroup1", "pass", "uhdf3453sdsdy252")
              ]

group_by_id = {g.id:g for g in group_list}
group_by_name = {g.name:g for g in group_list}