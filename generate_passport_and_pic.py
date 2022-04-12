import generate_passport
import generate_pic
import sys
id,bc = generate_passport.main(sys.argv[1], sys.argv[2])
generate_pic.main(id+".tgdpassport",bc)
