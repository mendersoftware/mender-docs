from readability import Readability
from readability.exceptions import ReadabilityException
import sys

if len(sys.argv) <= 1:
    print("No files given")
    sys.exit(1)

exit_code = 0

for file in sys.argv[1:]:
    with open(file) as f:
        text = f.read()
        r = Readability(text)
        try:
            gf = r.gunning_fog()
        except ReadabilityException as e:
            sys.exit(0)

        if not 9 <= int(gf.score) <= 12:
            print(
                "Gunning-Fog index for {} is {}, and not in the range [9, 12]".format(
                    file, gf.score
                )
            )
            exit_code = 1
        else:
            print("Gunning-Fox index for {} is {}".format(file, gf.score))

sys.exit(exit_code)
