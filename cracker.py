import crypt,optparse
from threading import Thread


def cmpPass(cryptPass, word, salt):
   cryptWord= crypt.crypt(word,salt)
   if (cryptWord == cryptPass):
      print ("[+] Found Password " +word)
   return
def testPass(cryptPass, dname):
   dicFile = open(dname,'r')
   salt = cryptPass.split('.')[0]
   for word in dicFile.readlines():
      word = word.strip('\n')
      t = Thread(target=cmpPass, args=(cryptPass, word, salt))
      t.start()
   return
def main():
   parser = optparse.OptionParser("usage%prog "+ "-f <password file> -d <dictionary>")
   parser.add_option('-f', dest='fname', type='string', help='specify password file')
   parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
   (options,args) = parser.parse_args()
   if (options.fname == None) | (options.dname == None):
      print (parser.usage)
      exit(0)
   else:
      fname = options.fname
      dname = options.dname

   passFile = open(fname)
   for line in passFile.readlines():
      if ":" in line:
         cryptPass=line.split(':')[1]
         t = Thread(target=testPass, args=(cryptPass, dname))
         t.start()
if __name__=="__main__":
   main()