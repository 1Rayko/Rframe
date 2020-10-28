require "colorize"
require 'fileutils'
puts """
   ___  ___                  
  / _ \/ _/______ ___ _  ___ 
 / , _/ _/ __/ _ `/  ' \/ -_)
/_/|_/_//_/  \_,_/_/_/_/\__/ 
                             
		by kotik06

""".red
FileUtils.cd('u')
print ("""
[1]-Zframe
[2]-VKtool
[3]-botvk
[4]-SILENt
[5]-qiwi_scam
[-->]""")
opt = gets.chomp.to_s

case opt
when '1'
	FileUtils.cd('Zframe-master')
	system('python GO.py')
when '2'
	FileUtils.cd('VKTOOL-master')
	system('python n.py')
when '3'
	FileUtils.cd('botvk-master')
	system('python botbilder.py')
when '4'
	FileUtils.cd('SILENt-master')
	system('python go.py')
when '5'
	FileUtils.cd('qiwi_scam-master')
	system('python qiwi_scam.py')

end