import numpy


class Version:
    def __init__(self, version: str):
        self.version = version

    def __eq__(self, other):
        self.version = list(self.version)
        other.version = list(other.version)
        if numpy.all(self.version == other.version):
            return True
        elif numpy.all(self.version != other.version):
            return False


def main():
    to_test = [
        ('1.0.0', '2.0.0'),
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
