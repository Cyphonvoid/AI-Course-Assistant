export class LED{
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
  
  //let led = new LED(20, 20)
  //document.body.appendChild(led.html());
  
  
  
  