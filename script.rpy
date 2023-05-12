# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character ("adriana")
define b = Character ("abner")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cena

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show abn at truecenter
    b " mãe! olha."
    b " esta é minha namorada"

    hide abn

    show mae at left
    a " nosssa !!"
    a " não tinha como arrumar coisa melhor ??"
    hide MAE

    show abn at truecenter
    b " mãe já deu !"
    b " eu a amo !"
    hide abn

    show mae at left
    a " eu não estou falando com voce !"

 

    # This ends the game.

    return
