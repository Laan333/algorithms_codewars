templates_basic = ["no one likes this",
                   "name likes this",
                   "name and name like this",
                   "name, name and name like this",
                   "name, name and num others like this"]


def likes(names: list):
    len_names = len(names)
    def create_gen(names: list, needed_template):
        for i in range(len(names)):
            needed_template = needed_template.replace('name', names[i], 1)
        if "num" in needed_template:
            needed_template = needed_template.replace('num', str(len_names - 2), 1)
        return needed_template
    if len_names < 4 > 0:
        needed_template = templates_basic[len_names]
        return create_gen(names, needed_template)
    elif len_names == 0:
        return templates_basic[0]
    else:
        needed_template = templates_basic[-1]
        return create_gen(names[:2], needed_template)

print(likes(['Peter']))
print('Peter likes this')
print(likes(['Peter']) == 'Peter likes this')
print(likes(['Sylvie', 'Quincy Rosenkreutz', 'Largo', 'Leon McNichol', 'Daley Wong', 'Priscilla S. Asagiri', 'Anri']))
