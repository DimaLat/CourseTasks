from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version: str):
        self.version = version
        self.first_part = self.get_first_part()
        self.second_part = self.get_second_part()

    def convert_to_one_format(self):
        """method for converting versions to one format"""

        version = self.version
        version = version.replace('-', '|')
        version = version.replace('alpha', 'a')
        version = version.replace('beta', 'b')
        version = version.replace('1b', '1|b')
        standard_format_version = version
        return standard_format_version

    def __eq__(self, other):
        return self.convert_to_one_format() == other.convert_to_one_format()

    def __gt__(self, other):
        if self.first_part != other.first_part:
            return self.first_part > other.first_part
        elif self.second_part == '':
            return True
        elif other.second_part == '':
            return False

    def get_first_part(self):
        """method for taking the first part from version which contains numbers"""

        if '|' in self.convert_to_one_format():
            first_part = self.convert_to_one_format().split('|')[0]
        else:
            first_part = self.version
        return first_part

    def get_second_part(self):
        """method for taking the second part from version which contains numbers and letters"""

        if '|' in self.convert_to_one_format():
            second_part = self.convert_to_one_format().split('|')[1]
        else:
            second_part = ''
        return second_part


def main():
    to_test = [
        ('1.0.0', '2.0.0'),
        ('1.0.1', '1.1.0'),
        ('1.0.0', '1.42.0'),
        ('1.2.0', '1.2.42'),
        ('1.1.0-alpha', '1.2.0-alpha.1'),
        ('1.0.1b', '1.0.10-alpha.beta'),
        ('1.0.0-rc.1', '1.0.0'),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), 'le failed'
        assert Version(version_2) > Version(version_1), 'ge failed'
        assert Version(version_2) != Version(version_1), 'neq failed'


if __name__ == "__main__":
    main()
