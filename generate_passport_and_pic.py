import generate_passport
import generate_pic
import sys
id = generate_passport.main(sys.argv[1], argv[2])
generate_pic.main(id+".tgdpassport")