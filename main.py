from tkinter import *

root = Tk()
root.title("TARGET_App")
root.geometry("800x400")
root['background'] = '#afeae6'
#root.configure(bg="")

# Creating a label widget
tagLabel = Label(root, text="Tag Name").place(x=400, y=60)
fileLabel = Label(root, text="Document Name").place(x=580, y=60)
parentTagLbl = Label(root, text="Parent Tag").place(x=400, y=200)
childTagsLbl = Label(root, text="Child Tags").place(x=580, y=200)
pathLabel = Label(root, text="File Path").place(x=30, y=15)

txtTag = Entry(root, width=10, borderwidth=5)
txtTag.place(x=393, y=90)
#e.insert(0, "Tag: ")
txtDoc = Entry(root, width=40, borderwidth=5)
txtDoc.place(x=500, y = 90)
txtParent = Entry(root, width=10, borderwidth=5)
txtParent.place(x=393, y=230)
txtChild = Entry(root, width=40, borderwidth=5)
txtChild.place(x=500, y = 230)
txtDocPath = Entry(root, width=50, borderwidth=5)
txtDocPath.place(x=30, y=40)

#tagEntry = txtTag.get()
docFile = {}
docRelation = {}

def tagDocClick():
    #myLabel2 = Label(root, text='The button was clicked')
    tagEntry = txtTag.get()
    docEntry = txtDoc.get()
    docFile[tagEntry] = docEntry
    # print(docFile)
    return docFile

def tagParentChildClick():
    parentTag = txtParent.get()
    childTag = txtChild.get()
    childTag = childTag.split(',')
    childTag = tuple(childTag)
    docRelation[parentTag] = childTag
    print(docRelation)
    return(docRelation)


tagFileBtn = Button(root, text='Enter', padx=40, pady=10, command=tagDocClick, bg = 'white')
tagFileBtn.place(x=640,y=140)
parentChildBtn = Button(root, text='Enter', padx=40, pady=10, command=tagParentChildClick, bg = 'white')
parentChildBtn.place(x=640, y=280)
createDocBtn = Button(root, text='Create Doc', padx=50, pady=20, command=tagParentChildClick,  bg = 'white')
createDocBtn.place(x=30, y=80)

# Create an event loop
root.mainloop()



