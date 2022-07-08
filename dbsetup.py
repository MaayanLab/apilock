from app import db, User, File, Collection, Role, UserRole, Policy, RolePolicy, PolicyCollections, PolicyFiles

db.drop_all()
db.create_all()

user_1 = User(name='Alexander Lachmann', 
                first_name="Alexander", 
                last_name="Lachmann",
                affiliation="Mount Sinai Hospital",
                email="alexander.lachmann@gmail.com")

user_2 = User(name='Avi Ma\'ayan', 
                first_name="Avi", 
                last_name="Ma\'ayan",
                affiliation="Mount Sinai Hospital",
                email="avi.maayan@mssm.edu")

user_3 = User(name='Daniel Clarke', 
                first_name="Daniel", 
                last_name="Clarke",
                affiliation="Mount Sinai Hospital",
                email="u8sand@sand.com")

root_collection = Collection(name="root", user=user_1)

file_1 = File(name="file_1.txt", user=user_1, collection=root_collection)
file_2 = File(name="file_2.txt", user=user_1, collection=root_collection)
file_3 = File(name="file_3.txt", user=user_1, collection=root_collection)

file_4 = File(name="file_4.txt", user=user_2, collection=root_collection)
file_5 = File(name="file_5.txt", user=user_2, collection=root_collection)
file_6 = File(name="file_6.txt", user=user_2, collection=root_collection)
file_7 = File(name="file_7.txt", user=user_2, collection=root_collection)

lyme_collection = Collection(name="lyme_data", user=user_3, parent=root_collection)

file_8 = File(name="file_8.txt", user=user_3, collection=lyme_collection)
file_9 = File(name="file_9.txt", user=user_3, collection=lyme_collection)
file_10 = File(name="file_10.txt", user=user_3, collection=lyme_collection)
file_11 = File(name="file_11.txt", user=user_3, collection=lyme_collection)

db.session.add_all([file_1, file_2, file_3, file_4, file_5, file_6, file_7, file_8, file_9, file_10, file_11])
db.session.commit()

policy_1 = Policy(effect="allow", action="list")
policy_2 = Policy(effect="allow", action="read")
policy_3 = Policy(effect="allow", action="write")

policy_1.collections.append(root_collection)
policy_2.collections.append(root_collection)

admin_role = Role(name="admin")
user_1.roles.append(admin_role)

base_reader = Role(name="base_reader")
base_reader.policies.append(policy_1)
base_reader.policies.append(policy_2)

policy_3 = Policy(effect="allow", action="list")
policy_3.collections.append(root_collection)


policy = Policy(effect="allow", action="list")
policy.collections.append(lyme_collection)
lyme_lister = Role(name="lyme_lister")
lyme_lister.policies.append(policy_3)

policy = Policy(effect="allow", action="read")
policy.collections.append(lyme_collection)
lyme_reader = Role(name="lyme_reader")
lyme_reader.policies.append(policy)

user_2.roles.append(lyme_lister)
user_1.roles.append(lyme_lister)
user_1.roles.append(lyme_reader)

db.session.add_all([])

db.session.commit()

