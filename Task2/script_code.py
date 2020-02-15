from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version: str):
        self.version = version

    def convert_to_one_format(self):
        """method for converting versions to one format"""

        version = self.version
        version = version.replace('-', '|')
        version = version.replace('alpha', 'a')
        version = version.replace('beta', 'b')
        version = version.replace('1b', '1-b')
        standard_version = version
        print(standard_version)
        return standard_version

    def __eq__(self, other):
        return self.convert_to_one_format() == other.convert_to_one_format()

    def __lt__(self, other):
        return self.convert_to_one_format() < other.convert_to_one_format()

    def get_letter_part(self):
        """method for taking letter part from version"""

        if '|' in self.convert_to_one_format():
            letter_part = self.convert_to_one_format().split('|')[1]
        else:
            letter_part = ''
        return letter_part

    def get_numeric_part(self):
        """method for taking numeric part from version"""

        if '|' in self.convert_to_one_format():
            numeric_part = self.convert_to_one_format().split('|')[0]
        else:
            numeric_part = version
        return numeric_part


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
