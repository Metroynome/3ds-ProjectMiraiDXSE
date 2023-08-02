##====CREDITS AND BIG THANKS=====##
##  THANK YOU TO ALL WHO HELPED  ##
##   MAKE THIS EDITOR POSSIBLE   ##
##      CREATOR: Agent Moose     ##
##          BIG THANKS TO:       ##
##  Shadowtrance, DaBlackDeath,  ##
##      AyanamiRei1, Vermil      ##
###################################
##  Yes, I was too lazy to make  ##
##   a new "Credits" section so  ##
##   I just copied the one from  ##
##    the original python code.  ##
##     Anyway, the Python GUI    ##
##       was created by me,      ##
##           Agent Moose         ##
###################################

try: #Python 2 imports
    from Tkinter import *
    import ttk
    import tkFileDialog as filedialog
    
except ImportError: #Python 3 imports
    from tkinter import *
    from tkinter import ttk
    from tkinter import filedialog

def openSave():
    global save
    save = filedialog.askopenfilename(initialdir="/", title = "Select file")
    if file == '':
        return
    else:
        SAVE.config(state="normal")

def ProjectDiva(Hatsune = 0x00, CloverClub = ''):
    Miku = 0x00
    for Rin in range(0,8):
        for Vocaloid in Songs:
            rawr.seek(Vocaloid + Hatsune + Miku)
            rawr.write(CloverClub)
        Miku += 0x10

def ProjectMirai(Megurine, Luka):
    for Vocaloid in Songs:
        Vocaloid += Megurine
        rawr.seek(Vocaloid)
        rawr.write(Luka)

def DivaArcade(Diva_X_Sucks):
    if (UnlockItems.get() or BuyItems.get()) == 1:
        # Unlock All Small Items in Shop
        for a in SmallItems[0]:
            rawr.seek(a)
            rawr.write(Diva_X_Sucks)
        # Unlock All Medium Items in Shop
        for a in MediumItems[0]:
            rawr.seek(a)
            rawr.write(Diva_X_Sucks)
        # Unlock All Large Items in Shop
        for a in LargeItems[0]:
            rawr.seek(a)
            rawr.write(Diva_X_Sucks)
        # Unlock all Air Items in Shop
        for a in AirItems[0]:
            rawr.seek(a)
            rawr.write(Diva_X_Sucks)
    if (UnlockOutfits.get() or BuyOutfits.get()) == 1:
        # Unlock All Outfits
        for a in Outfits:
            rawr.seek(a)
            rawr.write(Diva_X_Sucks)


def saveSave():
    global rawr
    print '===================================='
    with file(save, 'r+b') as rawr:
        if MaxMP.get() == 1:
            # Max MP (992244)
            rawr.seek(0x0008)
            rawr.write('\xF4\x23\x0F\x00')
            print 'MP Set to Max with no overflow! (992244)'
        if MaxFunds.get() == 1:
            # Max Parters' Funds! (99,999)
            # Credits to Vermil
            Funds = 0x00
            for Vermil in range(0, 8):
                rawr.seek(0x0024 + Funds)
                rawr.write('\x6F\x89\01\x00')
                Funds += 0x598
            print 'All Partners\' Funds set to 99,999!'
        if MaxSnacks.get() == 1:
            # Max Snacks! (Max the game lets you have is 9...dumb!)
            # Credits to DaBlackDeath and Shadowtrance for this tid-bit!
            for DaBlackTrance in range(0, 10):
                rawr.seek(0x0014 + DaBlackTrance)
                rawr.write('\x09')
            print 'All Snacks set to 9!'
        if UnlockSongs.get() == 1 and MaxRank.get() == 0:
            # Unlock All Songs
            ProjectMirai(0x98, '\xA0')
            print 'All 48 Songs Unlocked!'
        if UnlockHard.get() == 1:
            # Unlock Hard Button
            ProjectMirai(0x20, '\x01')
            # Unlock Super Hard Button
            ProjectMirai(0x30, '\x01')
            # Unlock Hard Touch
            ProjectMirai(0x60, '\x01')
            # Unlock Super Hard Touch
            ProjectMirai(0x70, '\x01')
            rawr.seek(0x21bc)
            rawr.write('\x6B\x0D\x00\x00\x11\x00\x00\x00\x52\x00\x65\x00\x69\x00\x00\x00')
            rawr.seek(0x21f0)
            rawr.write('\x09\x00\x09\x00\x09\x00\x09\x00\x09\x00\x09\x00\x2F\x36\x00\x00\x00\x98\x01\x00\x06')
            print 'All Hard Mode and Super Hard Mode difficulties Unlocked!'
        if MaxHighscore.get() == 1:
            ProjectDiva(0x04, '\x3f\x42\x0f\x00')
            print 'All Songs High Score set to 999,999!'
        if MaxPercentage.get() == 1:
            ProjectDiva(0x08, '\x00\x00\x80\x3F')
            print 'All Songs hit percentage set to 100.00%!'
        if MaxCombo.get() == 1:
            ProjectDiva(0x0e, '\xE7\x03')
            print 'All Songs Max Combo set to 999!'
        if MaxRank.get() == 1:
            ProjectDiva(0x00, '\x05')
            ProjectDiva(0x0c, '\x00')
            ProjectMirai(0x98, '\xAA')
            if MaxRank.get() == 1 and UnlockSongs.get() == 0:
                print 'All Songs set to \"Perfect\" Rank!'
            elif MaxRank.get() == 1 and UnlockSongs.get() == 1:
                print 'All Songs Unlocked and set to \"Perfect\" Rank!'
        if UnlockItems.get() == 1:
            DivaArcade('\x03')
            if UnlockItems.get() == 1 and BuyItems.get() == 0:
                print 'All Room Items in the shop Unlocked, but not paid for.'
        if UnlockOutfits.get() == 1:
            DivaArcade('\x03')
            if UnlockOutfits.get() == 1 and BuyOutfits.get() == 0:
                print 'All Outfits in the shop Unlocked, but not paid for.'
        if UnlockStamps.get() == 1:
            for Stamps in range(0, 115):
                rawr.seek(0x7B0C + Stamps)
                rawr.write('\x01')
            print 'All 115 Stamps Unlocked!'
        if UnlockProfileCard.get() == 1:
            for ProfileCard in range(0, 846):
                rawr.seek(0x7BB4 + ProfileCard)
                rawr.write('\x01')
            print 'All Profile Card Options Unlocked!'
        if BuyItems.get() == 1:
            DivaArcade('\x05')
            print 'All Room Items in the shop unlocked and paid for!'
        if BuyOutfits.get() == 1:
            DivaArcade('\x05')
            print 'All Outfits in the shop unlocked and paid for!'   

class CB(Frame):
   def get(self):
       return self.var.get()
   def __init__(self, parent=None, cheater=""):
        Frame.__init__(self, parent)
        self.var = BooleanVar()
        rawr = Checkbutton(self, text=cheater, variable=self.var, bg="white")
        rawr.pack()
        self.grid(sticky='w', columnspan=2)

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

pmdxse = Tk()
pmdxse.title("Project Mirai DX Save Editor")
pmdxse.configure(bg="white", padx=10, pady=10)
pmdxse.resizable(width=False, height=False)

Button(pmdxse, text="Open", command=openSave, width=8).grid(row=0, column=0)
SAVE = Button(pmdxse, text="Save", command=saveSave, state=DISABLED, width=8)
SAVE.grid(row=0, column=1)

MaxMP = CB(pmdxse, 'Max MP')
MaxFunds = CB(pmdxse, 'Max Partners Funds')
MaxSnacks = CB(pmdxse, 'Max Snacks')
UnlockSongs = CB(pmdxse, 'Unlock all Songs')
UnlockHard = CB(pmdxse, 'Unlock Hard/Super Hard Modes')
MaxHighscore = CB(pmdxse, 'Max Highscore on All Songs')
MaxPercentage = CB(pmdxse, 'Max Percentage on All Songs')
MaxCombo = CB(pmdxse, 'Max Combo on All Songs')
MaxRank = CB(pmdxse, 'Set each song to \"Perfect\" rank')
UnlockItems = CB(pmdxse, 'Unlock all Items in the Shop')
UnlockOutfits = CB(pmdxse, 'Unlock all Outfits')
UnlockStamps = CB(pmdxse, 'Unlock all 115 Stamps')
UnlockProfileCard = CB(pmdxse, 'Unlock all Profile Card Options')
BuyItems = CB(pmdxse, 'Buy all Items')
BuyOutfits = CB(pmdxse, 'Buy all Outfits')

Label(pmdxse, text="Created by Agent Moose", pady=10).grid(columnspan=2)


pmdxse.mainloop()
