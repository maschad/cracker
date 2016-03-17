import crypt,optparse,string,random
from threading import Thread

salt_chars = './' + string.ascii_letters + string.digits

def cmpPass(cryptPass, word, salt):
   cryptWord= crypt.crypt(word,salt)
   if (cryptWord == cryptPass):
      print ("[+] Found Password " +word)
   return

def testPass(cryptPass, dname):
   dicFile = open(dname,'r')
   salt = salt_chars[random.randint(0, 63)] + salt_chars[random.randint(0, 63)]
   for word in dicFile.readlines():
      word = word.strip('\n')
      t = Thread(target=cmpPass, args=(cryptPass, word, salt))
      t.start()
   return
   
def main():
   parser = optparse.OptionParser("usage%prog "+ "-f <file> -d <dictionary>")
   parser.add_option('-f', dest='fname', type='string', help='specify file to unlock')
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
         cryptPass = line.split(':')[1]
         t = Thread(target=testPass, args=(cryptPass, dname))
         t.start()

if __name__=="__main__":
   main()