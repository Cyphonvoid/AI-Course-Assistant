

class CollapseButton{

    constructor(){

    }

    Show(){
        
    }

    Hide(){

    }

}

class ChatBox {

   constructor(width, height) {
     this._frame = document.createElement('div')
     document.body.appendChild(this._frame)
     
     /*Creating Main frame of the Chat Box*/
     this.width = width;
     this.height = height; 

     this._frame.style.backgroundColor = "#242424"
     this._frame.style.borderColor = "red"
     this._frame.style.height = height + 'px'
     this._frame.style.width = width + 'px'
     this._frame.style.position = "absolute"
     this._frame.style.borderRadius = "10px 10px 10px 10px"
     this._frame.style.borderWidth = "10px";
     

     /*[PANEL] Creating a panel object for the frame*/
     this._panel = document.createElement('div')
     this._frame.appendChild(this._panel)

     this._panel.style.top = 0 + 'px'
     this._panel.style.left = 0 + 'px'
     this._panel.style.position = "absolute"
     this._panel.style.width = width + 'px'
     this._panel.style.height = 54 + 'px'
     this._panel.style.backgroundColor = "black"
     this._panel.style.borderRadius = "10px 10px 0px 0px"
     

     //Panel - Logout Button
     this._logout_button = document.createElement('button')
     this._panel.appendChild(this._logout_button)

     this._logout_button.style.width = 34 + 'px'
     this._logout_button.style.height = 34 + 'px'
     this._logout_button.style.position = "absolute"
     this._logout_button.style.top = "20%"
     this._logout_button.style.left = "4.5%"
     this._logout_button.style.backgroundColor = "blue"
     this._logout_button.style.borderRadius = "2px 2px 2px 2px"
     this._logout_button.textContent = ""


     //Panel - Company Title
     this._title = document.createElement('button')
     this._panel.appendChild(this._title)

     this._title.style.width = 120 + 'px'
     this._title.style.height = 40 + 'px'
     this._title.style.position = "absolute"
     this._title.style.top = "49%"
     this._title.style.left = "37%"
     this._title.style.backgroundColor = "black"
     this._title.style.borderRadius = "6px 6px 17px 17px"

     //Panel - Power Button

     this._power_button = document.createElement('button')
     this._panel.appendChild(this._power_button)

     this._power_button.style.width = 34 + 'px'
     this._power_button.style.height = 34 + 'px'
     this._power_button.style.position = "absolute"
     this._power_button.style.top = "20%"
     this._power_button.style.left = "87%"
     this._power_button.style.backgroundColor = "pink"
     this._power_button.style.borderRadius = "2px 2px 2px 2px"


    
     /*[TOOLBAR] Creating a bottom toolbar*/
     this._toolbar = document.createElement('div')
     this._frame.appendChild(this._toolbar)

     this._toolbar.style.width = this.width + 'px'
     this._toolbar.style.height = 55 + 'px'
     this._toolbar.style.top = (this.height - 55) + 'px'
     this._toolbar.style.left = 0 + 'px'
     this._toolbar.style.position = "absolute"
     this._toolbar.style.backgroundColor = "black"
     this._toolbar.style.borderRadius = "0px 0px 10px 10px"

     
     //Toolbar - Settings Button
     this._settings_button = document.createElement('button')
     this._toolbar.appendChild(this._settings_button)

     this._settings_button.style.width = 34 + 'px'
     this._settings_button.style.height = 34 + 'px'
     this._settings_button.style.position = "absolute"
     this._settings_button.style.top = "20%"
     this._settings_button.style.left = "5%"
     this._settings_button.style.backgroundColor = "blue"
     this._settings_button.style.borderRadius = "2px 2px 2px 2px"
     this._settings_button.textContent = ""


     //Toolbar - Help
     this._help_button = document.createElement('button')
     this._toolbar.appendChild(this._help_button)

     this._help_button.style.width = 34 + 'px'
     this._help_button.style.height = 34 + 'px'
     this._help_button.style.position = "absolute"
     this._help_button.style.top = "20%"
     this._help_button.style.left = "87%"
     this._help_button.style.backgroundColor = "blue"
     this._help_button.style.borderRadius = "2px 2px 2px 2px"
     this._help_button.textContent = ""

     //Toolbar - Send Button
     this._send_button = document.createElement('button')
     this._toolbar.appendChild(this._send_button)
 
     
     this._send_button.style.width = 120 + 'px'
     this._send_button.style.height = 34 + 'px'
     this._send_button.style.position = "absolute"
     this._send_button.style.top = "13px"
     this._send_button.style.left = "34%"
     this._send_button.style.backgroundColor = "#BE3838"
     this._send_button.style.borderRadius = "5px 5px 5px 5px"
     this._send_button.textContent = "Send Prompt"
     this._send_button.style.color = "white"
     this._send_button.style.fontSize = "16px"
     this._send_button.style.fontFamily = "Arial"
     this._send_button.style.fontWeight = "bold"
     this._send_button.style.opacity = "90%"
     
        this._send_button.addEventListener("mouseover", ()=>{this._send_button.style.opacity = "100%"})
        this._send_button.addEventListener("mouseout", ()=>{this._send_button.style.opacity = "90%"})
        this._send_button.addEventListener("click", ()=>{
          this.UserChannel()

          this._send_button.style.opacity = "50%"

          setTimeout(()=>{
            this._send_button.style.opacity = "90%"
          }, 90)
        })  

   }
 
   Show(){

   }

   Hide(){

   }
   
   MoveTo(X, Y){
    this._frame.style.top = Y + 'px'
    this._frame.style.left = X + 'px'
   }

   UserChannel(){
    console.log(" : got from input")
   }

   GeminiChannel(text){

   }

}

class AssistantAI {

    constructor(){
        this._collapse_state = false;
        this._Chat_UI = new ChatBox(430, 680)
        this._Collapse_Button = new CollapseButton()

        this._Chat_UI.MoveTo(110, 100)
        this.launch();
    }

    launch(){
        this._collapse_state = true; 
        this._Chat_UI.Hide()
        this._Collapse_Button.Show()
    }

    collapse(){
       this._collapse_state = true; 
       //Launch the Collapse button element and hide the box
       this._Chat_UI.Hide()
       this._Collapse_Button.Show()

    }

    expand(){
       this._collapse_state = false; 
       //Launch the box and hide the button
       this._Collapse_Button.Hide()
       this._Chat_UI.Show()

    }

    get_state(){
        return this._collapse_state; 
    }

}


//Launching the Assistant AI
let AI = new AssistantAI()
AI.expand()


