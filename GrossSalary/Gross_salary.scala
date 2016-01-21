class Gross_salary {
  private var basic:Double = 0.0
  private var hra: Double =0.0
  private var da:Double =0.0
  private var gross:Double =0.0

  def setBasic(basic:Double):Unit = {
    this.basic = basic;
  }
  def setGross(gross:Double){
    this.gross = gross;
  }
  
  
  def salary():Double = {


  if(basic >= 10000 && basic < 20000)  
    {  
        da = basic * 0.8;  
       hra = basic * 0.2;  
    }  
    else if(basic >= 20000 && basic < 30000)  
    {  
        da = basic * 0.9;  
        hra = basic * 0.25;  
    }  
    else if(basic >= 30000)  
    {  
        da = basic * 0.95;  
        hra = basic * 0.3;  
    }  
	
     basic + hra +da;

  }
} 