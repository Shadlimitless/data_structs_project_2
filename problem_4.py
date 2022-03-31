class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # Checking that the entry group is a parent
    if group.name != "parent" or len(user) == 0:
        return False
    def _is_user_in_group(user, group):
        user_ls = group.get_users()
        # Base case in case it goes up to last group without finding the user
        if not user in user_ls and len(group.get_groups()) == 0:
            return False
        if user in user_ls:
            return True
        else:
            group_ls = group.get_groups()
            for item in group_ls:
                return _is_user_in_group(user, item)

    return _is_user_in_group(user, group)



parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child_user = "child_user"
child.add_group(sub_child)
child.add_user(child_user)
parent.add_group(child)

print(is_user_in_group("sub_child_user", parent))
# # Will print True
print(is_user_in_group("child_user", parent))
# # Will print True
print(is_user_in_group("eeee", parent))
# Will print False because child is not in group

print(is_user_in_group("sub_child_user", child))
# Will print false even though the child has the sub-child, they dont have a parent in this call