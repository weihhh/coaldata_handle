import aiml
import os
os.chdir(r'D:\project\do_py\alice')
alice = aiml.Kernel()
alice.learn('startup.xml')
alice.respond('LOAD ALICE')
