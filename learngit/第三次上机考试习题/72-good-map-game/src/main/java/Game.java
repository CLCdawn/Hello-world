
/**
 * Created by Shifang on 2017/10/21.
 * 游戏类，请补全代码，如有必要，你可以添加一些方法
 */

public class Game {

    public Map map;

    /**
     *
     * @param initInfo 传入初始化参数,格式为:
     *                 M;x1,y1,hp1;x2,y2,hp2
     *                 分别表示
     *                 M : 棋盘宽度和高度(棋盘为方形)
     *                 x1,y1,hp1 : X 的初始位置,血量
     *                 x2,y2,hp2 : Y 的初始位置,血量
     */
    public Game(String initInfo){
    		String [] list = initInfo.split("");
    		int M = Integer.parseInt(list[0]);
    		int x1 = Integer.parseInt(list[2]);
    		int y1 = Integer.parseInt(list[4]);
    		int hp1 = Integer.parseInt(list[6]);
    		int x2 = Integer.parseInt(list[8]);
    		int y2 = Integer.parseInt(list[10]);
    		int hp2 = Integer.parseInt(list[12]);
    		Player p1 = new Player(x1, y1, hp1, "X");
    		Player p2 = new Player(x2, y2, hp2, "Y");
        map = new Map(M,p1,p2);

    }

    /**
     *
     * @param steps 传入两方依次走的步骤, X 先走, 两个玩家之间用","分开,
     *              每个玩家有 3 个参数,分别为'方向','是否攻击','是否隐身'
     *              方向用 U,D,L,R 分别表示上,下,左,右
     *              是否攻击,用 1 表示攻击,用0表示不攻击
     *              是否隐身,用 1 表示隐身,用0表示不隐身
     *              输入示例：
     *                U01,L10
     *              表示 X 向上走 1 步,不攻击,隐身; Y 向左走 1 步,攻击,不隐身
     *              在游戏过程中，如果有任意一方玩家角色死亡（生命值为 0 ），则对手胜利，比如若 X 生命值被减为 0 ，则输出 Y_WIN
     *              若走完所有的步骤,双方都没有死亡,则输出 DRAW
     * @return 游戏结果
     */
    public Result playGame(String steps){
    		Result re = null;
    		String[] stepList = steps.split(",");
    		map.print();
    		for(int i=0;i<stepList.length;i++) {
    			if(i%2==0) {
    				this.map.getd1().move(stepList[i].charAt(0));
    				if(stepList[i].charAt(1)=='1') {
    					if(map.getd1().calDistance(map.getd2())<=map.getd1().getGun().getRange()) {
    						this.map.getd2().changehp();
    					}
    				}
    				if(stepList[i].charAt(2)=='1') {
    					this.map.getd1().changeIsHide(true);;
    				}else {
    					this.map.getd1().changeIsHide(false);;
    				}
    			}else {
    				this.map.getd2().move(stepList[i].charAt(0));
    				if(stepList[i].charAt(1)=='1') {
    					if(map.getd2().calDistance(map.getd1())<=map.getd2().getGun().getRange()) {
    						this.map.getd1().changehp();
    					}
    				}
    				if(stepList[i].charAt(2)=='1') {
    					this.map.getd2().changeIsHide(true);;
    				}else {
    					this.map.getd2().changeIsHide(false);;
    				}
    			}
    			if(this.map.move()==Result.X_WIN) {
    				re = Result.X_WIN;
    				map.print();
    				break;
    			}else if(this.map.move()==Result.Y_WIN) {
    				re = Result.Y_WIN;
    				map.print();
    				break;
    			}else {
    				re = Result.DRAW;
    				map.print();
    			}
    		}	
        return re;
    }
    
    
}
