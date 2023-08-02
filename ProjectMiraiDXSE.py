import sys;

##====CREDITS AND BIG THANKS=====##
##  THANK YOU TO ALL WHO HELPED  ##
##   MAKE THIS EDITOR POSSIBLE   ##
##      CREATOR: Agent Moose     ##
##          BIG THANKS TO:       ##
## Shadowtrance and DaBlackDeath ##
##          for their GUI:       ##
## http://tinyurl.com/PMDXSE-GUI ##
##         AND AyanamiRei1       ##
##   for his help with finding   ##
##         Super Hard Mode       ##
###################################

#NOTE: 48 Songs in Total

#Easy Button First Rank Offset: 0x00
#Easy Button High Score Offset: 0x04
#Easy Button Percentage Offset: 0x08
#Easy Button Second Rank Offset: 0x0c
#Easy Button Combo Offset: 0x0e
#Normal Button First Rank Offset: 0x10
#Normal Button High Score Offset: 0x14
#Normal Button Percentage Offset: 0x18
#Normal Button Second Rank Offset: 0x1c
#Normal Button Combo Offset: 0x1e
#Hard Button First Rank Offset: 0x20
#Hard Button High Score Offset: 0x24
#Hard Button Percentage Offset: 0x28
#Hard Button Second Rank Offset: 0x2c
#Hard Button Combo Offset: 0x2e
#Super Hard Button First Rank Offset: 0x30
#Super Hard Button High Score Offset: 0x34
#Super Hard Button Percentage Offset: 0x38
#Super Hard Button Second Rank Offset: 0x3c
#Super Hard Button Combo Offset: 0x3e

#Easy Touch First Rank Offset: 0x40
#Easy Touch High Score Offset: 0x44
#Easy Touch Percentage Offset: 0x48
#Easy Touch Second Rank Offset: 0x4c
#Easy Touch Combo Offset: 0x4e
#Normal Touch First Rank Offset: 0x50
#Normal Touch High Score Offset: 0x54
#Normal Touch Percentage Offset: 0x58
#Normal Touch Second Rank Offset: 0x5c
#Normal Touch Combo Offset: 0x5e
#Hard Touch First Rank Offset: 0x60
#Hard Touch High Score Offset: 0x64
#Hard Touch Percentage Offset: 0x68
#Hard Touch Second Rank Offset: 0x6c
#Hard Touch Combo Offset: 0x6e
#Super Hard Touch First Rank Offset: 0x70
#Super Hard Touch High Score Offset: 0x74
#Super Hard Touch Percentage Offset: 0x78
#Super Hard Touch Second Rank Offset: 0x7c
#Super Hard Touch Combo Offset: 0x7e

#Unlock Song Offset: 0x98

Songs = [0x2750, 0x2848, 0x2940, 0x2A38, 0x2B30, 0x2C28, 0x2D20, 0x2E18, 0x2F10, 0x3008, 0x3100, 0x31F8, 0x32F0, 0x33E8, 0x34E0, 0x35D8, 0x36D0, 0x37C8, 0x38C0, 0x39B8, 0x3AB0, 0x3BA8, 0x3CA0, 0x3D98, 0x3E90, 0x3F88, 0x4080, 0x4178, 0x4270, 0x4368, 0x4460, 0x4558, 0x4650, 0x4748, 0x4840, 0x4938, 0x4A30, 0x4B28, 0x4C20, 0x4D18, 0x4E10, 0x4F08, 0x5000, 0x50F8, 0x51F0, 0x52E8, 0x53E0, 0x54D8, 0x55D0];

#First List in each list are the items that can be unlocked
#Second List in each list are each items in that catagory
SmallItems = [[0x6a28, 0x6a40, 0x6a48, 0x6a58, 0x6a60, 0x6a78, 0x6a88, 0x6a90, 0x6ac8, 0x6ad0, 0x6ad8, 0x6af0, 0x6af8], [0x69c0, 0x69c8, 0x69d0, 0x69d8, 0x69e0, 0x69e8, 0x69f0, 0x69f8, 0x6a00, 0x6a08, 0x6a10, 0x6a18, 0x6a20, 0x6a28, 0x6a30, 0x6a38, 0x6a40, 0x6a48, 0x6a50, 0x6a58, 0x6a60, 0x6a68, 0x6a70, 0x6a78, 0x6a80, 0x6a88, 0x6a90, 0x6a98, 0x6aa0, 0x6aa8, 0x6ab0, 0x6ab8, 0x6ac0, 0x6ac8, 0x6ad0, 0x6ad8, 0x6ae0, 0x6ae8, 0x6af0, 0x6af8, 0x6b00]];
MediumItems = [[0x6bd8, 0x6c10, 0x6c80], [0x6b50, 0x6B58, 0x6B60, 0x6B68, 0x6B70, 0x6B78, 0x6B80, 0x6B88, 0x6B88, 0x6B98, 0x6BA0, 0x6BA8, 0x6BB0, 0x6BB8, 0x6BC0, 0x6BC8, 0x6BD0, 0x6BD8, 0x6BE0, 0x6BE8, 0x6BF0, 0x6BF8, 0x6C00, 0x6C08, 0x6C10, 0x6C18, 0x6C20, 0x6C28, 0x6C30, 0x6C38, 0x6C40, 0x6C48, 0x6C50, 0x6C58, 0x6C60, 0x6C68, 0x6C70, 0x6C78, 0x6c80]];
LargeItems = [[0x6d38], [0x6CE0, 0x6CE8, 0x6CF0, 0x6CF8, 0x6D00, 0x6D08, 0x6D10, 0x6D18, 0x6D20, 0x6D28, 0x6D30, 0x6D38]];
WallItems = [0x6D80, 0x6D88, 0x6D90, 0x6D98, 0x6DA0, 0x6DA8, 0x6DB0, 0x6DB8, 0x6DC0, 0x6DC8, 0x6DD0, 0x6DD8, 0x6DE0, 0x6DE8, 0x6DF0, 0x6DF8, 0x6E00, 0x6E08, 0x6E10];
AirItems = [[0x6e90], [0x6e70, 0x6e78, 0x6e80, 0x6e88, 0x6e90]];
PoolItems = [0x6EC0, 0x6EC8, 0x6ED0, 0x6ED8];

Outfits = [0x56c8, 0x56E8, 0x5708, 0x5728, 0x5748, 0x5768, 0x5788, 0x57A8, 0x57C8, 0x57E8, 0x5808, 0x5828, 0x5848, 0x5868, 0x5888, 0x58A8, 0x58C8, 0x58E8, 0x5908, 0x5928, 0x5948, 0x5968, 0x5988, 0x59A8, 0x59C8, 0x59E8, 0x5A08, 0x5A28, 0x5A48, 0x5A68, 0x5A88, 0x5AA8, 0x5AC8, 0x5AE8, 0x5B08, 0x5B28, 0x5B48, 0x5B68, 0x5B88, 0x5BA8, 0x5BC8, 0x5C08, 0x5C28, 0x5C48, 0x5C68, 0x5C88, 0x5CA8, 0x5CC8, 0x5CE8, 0x5D08, 0x5D28, 0x5D48, 0x5D68, 0x5D88, 0x5DA8, 0x5DC8, 0x5DE8, 0x5E08, 0x5E28, 0x5E48, 0x5E68, 0x5E88, 0x5EA8, 0x5EC8, 0x5EE8, 0x5F08, 0x5F28, 0x5F48, 0x5F68, 0x5F88, 0x5FC8, 0x5FE8, 0x6008, 0x6028, 0x6048, 0x6068, 0x6088, 0x60A8, 0x60C8, 0x6108, 0x6128, 0x6148, 0x6168, 0x6188, 0x61A8, 0x61C8, 0x61E8, 0x6228, 0x6248, 0x6268, 0x6288, 0x62A8, 0x62C8, 0x62E8, 0x6328, 0x6348, 0x6368, 0x6388, 0x63A8, 0x63C8, 0x63E8, 0x6408, 0x6428, 0x6468, 0x6488, 0x64A8, 0x64C8, 0x64E8, 0x6508, 0x6548, 0x6568, 0x6588, 0x65A8, 0x65C8, 0x65E8, 0x6608, 0x6628, 0x6648, 0x6668, 0x6688];


with file(sys.argv[1], 'r+b') as rawr:
    if sys.argv[2] == "MaxMP":
        # Max MP (992244)
        rawr.seek(0x0008)
        rawr.write('\xF4\x23\x0F\x00')
        print 'MP Set to Max with no overflow! (992244)'
    elif sys.argv[2] == "UnlockSongs":
        # Unlock All Songs
        for AgentMoose in Songs:
            AgentMoose += 0x98
            rawr.seek(AgentMoose)
            rawr.write('\xA0')
        print 'All 48 Songs Unlocked!'
    elif sys.argv[2] == "UnlockHard":
        # Unlock Hard Button
        for deathwilldie in Songs:
            deathwilldie += 0x20
            rawr.seek(deathwilldie)
            rawr.write('\x01')
        # Unlock Super Hard Button
        for StarKiller in Songs:
            StarKiller += 0x30
            rawr.seek(StarKiller)
            rawr.write('\x01')
        # Unlock Hard Touch
        for SpankrPoodle in Songs:
            SpankrPoodle += 0x60
            rawr.seek(SpankrPoodle)
            rawr.write('\x01')
        # Unlock Super Hard Touch
        for BlackCrest in Songs:
            BlackCrest += 0x70
            rawr.seek(BlackCrest)
            rawr.write('\x01')
        rawr.seek(0x21bc)
        rawr.write('\x6B\x0D\x00\x00\x11\x00\x00\x00\x52\x00\x65\x00\x69\x00\x00\x00')
        rawr.seek(0x21f0)
        rawr.write('\x09\x00\x09\x00\x09\x00\x09\x00\x09\x00\x09\x00\x2F\x36\x00\x00\x00\x98\x01\x00\x06')
        print 'All Hard Mode and Super Hard Mode difficulties Unlocked!'
    elif sys.argv[2] == "UnlockItems":
        # Unlock All Small Items in Shop
        for a in SmallItems[0]:
            rawr.seek(a)
            rawr.write('\x03')
        # Unlock All Medium Items in Shop
        for a in MediumItems[0]:
            rawr.seek(a)
            rawr.write('\x03')
        # Unlock All Large Items in Shop
        for a in LargeItems[0]:
            rawr.seek(a)
            rawr.write('\x03')
        # Unlock all Air Items in Shop
        for a in AirItems[0]:
            rawr.seek(a)
            rawr.write('\x03')
        print 'All Room Items in the shop Unlocked, but not paid for.'
    elif sys.argv[2] == "UnlockOutfits":
        # Unlock All Outfits
        for a in Outfits:
            rawr.seek(a)
            rawr.write('\x03')
        print 'All Outfits in the shop Unlocked, but not paid for.'
    elif sys.argv[2] == "UnlockStamps":
        for Stamps in range(0, 115):
            rawr.seek(0x7B0C + Stamps)
            rawr.write('\x01')
        print 'All 115 Stamps Unlocked!'
    elif sys.argv[2] == "MaxHighScore":
        # All Easy Button High Score = 999999
        for EBH in Songs:
            EBH += 0x04
            rawr.seek(EBH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Normal Button High Score = 999999
        for NBH in Songs:
            NBH += 0x14
            rawr.seek(NBH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Hard Button High Score = 999999
        for HBH in Songs:
            HBH += 0x24
            rawr.seek(HBH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Super Hard Button High Score = 999999
        for SHBH in Songs:
            SHBH += 0x34
            rawr.seek(SHBH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Easy Touch High Score = 999999
        for ETH in Songs:
            ETH += 0x44
            rawr.seek(ETH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Normal Touch High Score = 999999
        for NTH in Songs:
            NTH += 0x54
            rawr.seek(NTH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Hard Touch High Score = 999999
        for HTH in Songs:
            HTH += 0x64
            rawr.seek(HTH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Super Hard Touch High Score = 999999
        for SHTH in Songs:
            SHTH += 0x74
            rawr.seek(SHTH)
            rawr.write('\x3f\x42\x0f\x00')
        print 'All Songs High Score at 999,999!'
    elif sys.argv[2] == "MaxPercentage":
        # All Easy Button Percentage = 100.00%
        for EBP in Songs:
            EBP += 0x08
            rawr.seek(EBP)
            rawr.write('\x00\x00\x80\x3F')
        # All Normal Button Percentage = 100.00%
        for NBP in Songs:
            NBP += 0x18
            rawr.seek(NBP)
            rawr.write('\x00\x00\x80\x3F')
        # All Hard Button Percentage = 100.00%
        for HBP in Songs:
            HBP += 0x28
            rawr.seek(HBP)
            rawr.write('\x00\x00\x80\x3F')
        # All Super Hard Button Percentage = 100.00%
        for SHBP in Songs:
            SHBP += 0x38
            rawr.seek(SHBP)
            rawr.write('\x00\x00\x80\x3F')
        # All Easy Touch Percentage = 100.00%
        for ETP in Songs:
            ETP += 0x48
            rawr.seek(ETP)
            rawr.write('\x00\x00\x80\x3F')
        # All Normal Touch Percentage = 100.00%
        for NTP in Songs:
            NTP += 0x58
            rawr.seek(NTP)
            rawr.write('\x00\x00\x80\x3F')
        # All Hard Touch Percentage = 100.00%
        for HTP in Songs:
            HTP += 0x68
            rawr.seek(HTP)
            rawr.write('\x00\x00\x80\x3F')
        # All Super Hard Touch Percentage = 100.00%
        for SHTP in Songs:
            SHTP += 0x78
            rawr.seek(SHTP)
            rawr.write('\x00\x00\x80\x3F')
        print 'All Songs hit percentage at 100.00%!'
    elif sys.argv[2] == "MaxCombo":
        # All Easy Button Combo = 999
        for EBC in Songs:
            EBC += 0x0e
            rawr.seek(EBC)
            rawr.write('\xE7\x03')
        # All Normal Button Combo = 999
        for NBC in Songs:
            NBC += 0x1e
            rawr.seek(NBC)
            rawr.write('\xE7\x03')
        # All Hard Button Combo = 999
        for HBC in Songs:
            HBC += 0x2e
            rawr.seek(HBC)
            rawr.write('\xE7\x03')
        # All Super Hard Button Combo = 999
        for SHBC in Songs:
            SHBC += 0x3e
            rawr.seek(SHBC)
            rawr.write('\xE7\x03')
        # All Easy Touch Combo = 999
        for ETC in Songs:
            ETC += 0x4e
            rawr.seek(ETC)
            rawr.write('\xE7\x03')
        # All Normal Touch Combo = 999
        for NTC in Songs:
            NTC += 0x5e
            rawr.seek(NTC)
            rawr.write('\xE7\x03')
        # All Hard Touch Combo = 999
        for HTC in Songs:
            HTC += 0x6e
            rawr.seek(HTC)
            rawr.write('\xE7\x03')
        # All Super Hard Touch Combo = 999
        for SHTC in Songs:
            SHTC += 0x7e
            rawr.seek(SHTC)
            rawr.write('\xE7\x03')
        print 'All Songs Max Combo at 999!'
    elif sys.argv[2] == "MaxSnacks":
        # Max Snacks! (Max the game lets you have is 9...dumb!)
        # Credits to DaBlackDeath and Shadowtrance for this tid-bit!
        for DaBlackTrance in range(0, 10):
            rawr.seek(0x0014 + DaBlackTrance)
            rawr.write('\x09')
        print 'All Snacks set to 9!'
    elif sys.argv[2] == "UnlockProfileOptions":
        for ProfileCard in range(0, 846):
            rawr.seek(0x7BB4 + ProfileCard)
            rawr.write('\x01')
        print 'All Profile Card Options Unlocked!'
    elif sys.argv[2] == "Perfect":
        # Perfect Each Song (I actually have no clue what writing AA does)
        for AgentMoose in Songs:
            AgentMoose += 0x98
            rawr.seek(AgentMoose)
            rawr.write('\xAA')
        # All Easy Button Rank = Perfect
        for Wrench_King in Songs:
            Wrench_King += 0x00
            rawr.seek(Wrench_King)
            rawr.write('\x05')
        # All Easy Button High Score = 999999
        for EBH in Songs:
            EBH += 0x04
            rawr.seek(EBH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Easy Button Percentage = 100.00%
        for EBP in Songs:
            EBP += 0x08
            rawr.seek(EBP)
            rawr.write('\x00\x00\x80\x3F')
        # All Easy Button Second Rank = S+
        for Nirvash_TypeZero in Songs:
            Nirvash_TypeZero += 0x0c
            rawr.seek(Nirvash_TypeZero)
            rawr.write('\x00')
        # All Easy Button Combo = 999
        for EBC in Songs:
            EBC += 0x0e
            rawr.seek(EBC)
            rawr.write('\xE7\x03')
        # All Normal Button Rank = Perfect
        for Badger41 in Songs:
            Badger41 += 0x10
            rawr.seek(Badger41)
            rawr.write('\x05')
        # All Normal Button High Score = 999999
        for NBH in Songs:
            NBH += 0x14
            rawr.seek(NBH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Normal Button Percentage = 100.00%
        for NBP in Songs:
            NBP += 0x18
            rawr.seek(NBP)
            rawr.write('\x00\x00\x80\x3F')
        # All Normal Button Second Rank = S+
        for sKiLLz in Songs:
            sKiLLz += 0x1c
            rawr.seek(sKiLLz)
            rawr.write('\x00')
        # All Normal Button Combo = 999
        for NBC in Songs:
            NBC += 0x1e
            rawr.seek(NBC)
            rawr.write('\xE7\x03')
        # All Hard Button Rank = Perfect
        for deathwilldie in Songs:
            deathwilldie += 0x20
            rawr.seek(deathwilldie)
            rawr.write('\x05')
        # All Hard Button High Score = 999999
        for HBH in Songs:
            HBH += 0x24
            rawr.seek(HBH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Hard Button Percentage = 100.00%
        for HBP in Songs:
            HBP += 0x28
            rawr.seek(HBP)
            rawr.write('\x00\x00\x80\x3F')
        # All Hard Button Second Rank = S+
        for reDFlag in Songs:
            reDFlag += 0x2c
            rawr.seek(reDFlag)
            rawr.write('\x00')
        # All Hard Button Combo = 999
        for HBC in Songs:
            HBC += 0x2e
            rawr.seek(HBC)
            rawr.write('\xE7\x03')
        # All Super Hard Button Rank = Perfect
        for DefyLogic in Songs:
            DefyLogic += 0x30
            rawr.seek(DefyLogic)
            rawr.write('\x05')
        # All Super Hard Button High Score = 999999
        for SHBH in Songs:
            SHBH += 0x34
            rawr.seek(SHBH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Super Hard Button Percentage = 100.00%
        for SHBP in Songs:
            SHBP += 0x38
            rawr.seek(SHBP)
            rawr.write('\x00\x00\x80\x3F')
        # All Super Hard Button Second Rank = S+
        for King_Geo in Songs:
            King_Geo += 0x3c
            rawr.seek(King_Geo)
            rawr.write('\x00')
        # All Super Hard Button Combo = 999
        for SHBC in Songs:
            SHBC += 0x3e
            rawr.seek(SHBC)
            rawr.write('\xE7\x03')
        # All Easy Touch Rank = Perfect
        for Vernon in Songs:
            Vernon += 0x40
            rawr.seek(Vernon)
            rawr.write('\x05')
        # All Easy Touch High Score = 999999
        for ETH in Songs:
            ETH += 0x44
            rawr.seek(ETH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Easy Touch Percentage = 100.00%
        for ETP in Songs:
            ETP += 0x48
            rawr.seek(ETP)
            rawr.write('\x00\x00\x80\x3F')
        # All Easy Touch Second Rank = S+
        for eYeDoL in Songs:
            eYeDoL += 0x4c
            rawr.seek(eYeDoL)
            rawr.write('\x00')
        # All Easy Touch Combo = 999
        for ETC in Songs:
            ETC += 0x4e
            rawr.seek(ETC)
            rawr.write('\xE7\x03')
        # All Normal Touch Rank = Perfect
        for SpankrPoodle in Songs:
            SpankrPoodle += 0x50
            rawr.seek(SpankrPoodle)
            rawr.write('\x05')
        # All Normal Touch High Score = 999999
        for NTH in Songs:
            NTH += 0x54
            rawr.seek(NTH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Normal Touch Percentage = 100.00%
        for NTP in Songs:
            NTP += 0x58
            rawr.seek(NTP)
            rawr.write('\x00\x00\x80\x3F')
        # All Normal Touch Second Rank = S+
        for destructo in Songs:
            destructo += 0x5c
            rawr.seek(destructo)
            rawr.write('\x00')
        # All Normal Touch Combo = 999
        for NTC in Songs:
            NTC += 0x5e
            rawr.seek(NTC)
            rawr.write('\xE7\x03')
        # All Hard Touch Rank = Perfect
        for A051019194709_2 in Songs:
            A051019194709_2 += 0x60
            rawr.seek(A051019194709_2)
            rawr.write('\x05')
        # All Hard Touch High Score = 999999
        for HTH in Songs:
            HTH += 0x64
            rawr.seek(HTH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Hard Touch Percentage = 100.00%
        for HTP in Songs:
            HTP += 0x68
            rawr.seek(HTP)
            rawr.write('\x00\x00\x80\x3F')
        # All Hard Touch Second Rank = S+
        for A051019194709_1 in Songs:
            A051019194709_1 += 0x6c
            rawr.seek(A051019194709_1)
            rawr.write('\x00')
        # All Hard Touch Combo = 999
        for HTC in Songs:
            HTC += 0x6e
            rawr.seek(HTC)
            rawr.write('\xE7\x03')
        # All Super Hard Touch Rank = Perfect
        for CriticalNova in Songs:
            CriticalNova += 0x70
            rawr.seek(CriticalNova)
            rawr.write('\x05')
        # All Super Hard Touch High Score = 999999
        for SHTH in Songs:
            SHTH += 0x74
            rawr.seek(SHTH)
            rawr.write('\x3f\x42\x0f\x00')
        # All Super Hard Touch Percentage = 100.00%
        for SHTP in Songs:
            SHTP += 0x78
            rawr.seek(SHTP)
            rawr.write('\x00\x00\x80\x3F')
        # All Super  Hard Touch Second Rank = S+
        for Chidori in Songs:
            Chidori += 0x7c
            rawr.seek(Chidori)
            rawr.write('\x00')
        # All Super Hard Touch Combo = 999
        for SHTC in Songs:
            SHTC += 0x7e
            rawr.seek(SHTC)
            rawr.write('\xE7\x03')
        # Unlock Super Hard Mode
        rawr.seek(0x21bc)
        rawr.write('\x6B\x0D\x00\x00\x11\x00\x00\x00\x52\x00\x65\x00\x69\x00\x00\x00')
        rawr.seek(0x21f0)
        rawr.write('\x09\x00\x09\x00\x09\x00\x09\x00\x09\x00\x09\x00\x2F\x36\x00\x00\x00\x98\x01\x00\x06')
        print 'All Songs Unlocked and at Perfect Rank, Max High Score, 100.00% Percentage Hit and Max Combo!'
        # Buy All Small Items in Shop
        for a in SmallItems[1]:
            rawr.seek(a)
            rawr.write('\x05')
        # Buy All Medium Items in Shop
        for a in MediumItems[1]:
            rawr.seek(a)
            rawr.write('\x05')
        # Buy All Large Items in Shop
        for a in LargeItems[1]:
            rawr.seek(a)
            rawr.write('\x05')
        # Buy All Wall Items in Shop
        for a in WallItems:
            rawr.seek(a)
            rawr.write('\x05')
        # Buy all Air Items in Shop
        for a in AirItems[1]:
            rawr.seek(a)
            rawr.write('\x05')
        # Buy all Air Items in Shop
        for a in PoolItems:
            rawr.seek(a)
            rawr.write('\x05')
        print 'All Room Items in the shop unlocked and paid for!'
        # Buy all Outfits
        for a in Outfits:
            rawr.seek(a)
            rawr.write('\x05')
        print 'All Outfits in the shop unlocked and paid for!'
        for Stamps in range(0, 115):
            rawr.seek(0x7B0C + Stamps)
            rawr.write('\x01')
        print 'All 115 Stamps Unlocked!'
        for ProfileCard in range(0, 846):
            rawr.seek(0x7BB4 + ProfileCard)
            rawr.write('\x01')
        print 'All Profile Card Options Unlocked!'


print 'All done, you cheater. ;)'
