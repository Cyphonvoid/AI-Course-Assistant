
class LED{
    constructor(width, height){
      this._led = document.createElement('div')
      this.width = width; 
      this.height = height; 
      this.color = "green";
      this._led.style.backgroundColor = "green";
      this._led.style.width = this.width + 'px';
      this._led.style.height = this.height + 'px'; 
      this._led.style.position = "absolute";
      this._state = false;
    }
  
    TurnOn(){
      this._led.style.backgroundColor = this.color; 
      this._state = true; 
    }
  
    TurnOff(){
      this._led.style.backgroundColor = "grey"; 
      this._state = false; 
    }
    
    MoveTo(x, y){
        this._led.style.top = y + 'px'; 
        this._led.style.left = x + 'px'; 
    }
    
    GetState(){
        return this._state; 
    }
    
    SetColor(color){
      this.color = color
      this._led.style.backgroundColor = color
    }
  
    html(){
        return this._led;
    }
  
    style(){
      return this._led.style
    }
    
    __sleep(seconds){
        return new Promise(resolve => setTimeout(resolve, 1000*seconds));
    }
  
    async Blink(num, time){
        let state = this.GetState();
        for(let i = 0; i < num; i++){
            this.TurnOff()
            await this.__sleep(time)
            this.TurnOn()
            await this.__sleep(time)
        }
    }
  }

  
class CollapseButton{

    constructor(){

    }

    Show(){
        
    }

    Hide(){

    }
}

class ChatBox {

   constructor() {
     this._container = document.createElement('div')
     this._container.style.backgroundColor = "green"
     this._container.textContent = "Hello world new extension"
     this._container.style.borderColor = "black"
     this._container.style.width = 40 + "px"
     this._container.style.height = 50 + "px"
     this._container.style.position = "absolute"
     
     this.MoveTo(90, 50)

     this._led = new LED(90, 90)
     
     document.body.appendChild(this._container);
     document.body.appendChild(this._led.html())

     this._led.MoveTo(300, 300)
     this._led.SetColor("red")
     this._led.Blink(20, 0.3)
   }

   Show(){

   }

   Hide(){

   }
   
   MoveTo(x, y){
    this._container.style.left = x + 'px';
    this._container.style.top = y + 'px'; 
   }

   html(){
     return this._container
    }

}

class AssistantAI {

    constructor(){
        this._collapse_state = true;
        this._Chat_UI = new ChatBox()
        this._Collapse_Button = new CollapseButton()
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


