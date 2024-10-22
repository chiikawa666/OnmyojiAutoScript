from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class PetsAssets: 


	# Image Rule Assets
	# 宠物小屋 
	I_PET_HOUSE = RuleImage(roi_front=(1012,414,56,25), roi_back=(952,412,144,60), threshold=0.7, method="Template matching", file="./tasks/Pets/pet/pet_pet_house.png")
	# 爪印 
	I_PET_CLAW = RuleImage(roi_front=(1171,625,55,56), roi_back=(1171,625,55,56), threshold=0.8, method="Template matching", file="./tasks/Pets/pet/pet_pet_claw.png")
	# 其乐融融 
	I_PET_HAPPY = RuleImage(roi_front=(853,614,67,70), roi_back=(853,614,67,70), threshold=0.8, method="Template matching", file="./tasks/Pets/pet/pet_pet_happy.png")
	# 大餐 
	I_PET_FEAST = RuleImage(roi_front=(0, 0, 1280, 720), roi_back=(0, 0, 1280, 720), threshold=0.8, method="Template matching", file="./tasks/Pets/pet/pet_pet_feast.png")
	# 玩耍 
	I_PET_PLAY = RuleImage(roi_front=(788,500,75,75), roi_back=(788,500,75,75), threshold=0.8, method="Template matching", file="./tasks/Pets/pet/pet_pet_play.png")
	# 投喂 
	I_PET_FEED = RuleImage(roi_front=(798,497,77,81), roi_back=(798,497,77,81), threshold=0.8, method="Template matching", file="./tasks/Pets/pet/pet_pet_feed.png")
	# 跳过 
	I_PET_SKIP = RuleImage(roi_front=(1089,119,72,41), roi_back=(999,42,242,147), threshold=0.65, method="Template matching", file="./tasks/Pets/pet/pet_pet_skip.png")
	# 退出 
	I_PET_EXIT = RuleImage(roi_front=(30,25,39,33), roi_back=(30,25,39,33), threshold=0.8, method="Template matching", file="./tasks/Pets/pet/pet_pet_exit.png")


	# Ocr Rule Assets
	# 投喂的体力 
	O_PET_FEED_AP = RuleOcr(roi=(730,527,57,33), area=(730,527,57,33), mode="Digit", method="Default", keyword="", name="pet_feed_ap")
	# 玩耍的体力 
	O_PET_PLAY_GOLD = RuleOcr(roi=(681,524,74,40), area=(681,524,74,40), mode="Digit", method="Default", keyword="", name="pet_play_gold")


