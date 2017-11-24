import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
class frontEnd extends JFrame{
	JPanel panel= new JPanel();
	XOButton buttons[]= new XOButton[9];

	public static void main(String arge[]){
		new frontEnd();
	}
	frontEnd(){
		super("frontEnd");
		setSize(400,400);
		setResizable(false);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		panel.setLayout(new GridLayout(3,3));
		for(int i=0;i<9;i++){
			buttons[i] = new XOButton();
			buttons[i].setText(Integer.toString(i));
			panel.add(buttons[i]);
		}
		add(panel);
		setVisible(true);

	}
}
class BackEnd {
	public static byte[][] board= new byte[3][3];
	public static byte player=1;
	public static boolean isEmpty(int pos){
		int i=pos/3,j=pos%3;
		if(board[i][j]==0){
			//make move
			board[i][j]=player;
			return true;
		}
		return false;
	}
	public static boolean checkWin(){
		boolean check1=true,check2=true;
		for(int i=0;i<3;i++){
			check1=check2=true;
			for(int j=0;j<3;j++){
				if(board[i][j]!=player)
					check1=false;
				if(board[j][i]!=player)
					check2=false;
			}
			if(check1)
				return true;
			if(check2)
				return true;
		}
		if(board[0][0]==player && board[1][1]==player && board[2][2]==player)
			return true;
		if(board[0][2]==player && board[1][1]==player && board[2][0]==player)
			return true;
		return false;
	}
	public static void setPlayer(){
		if(player==1)
			player=2;
		else
			player=1;
	}
	public static boolean checkTie(){
		for(int i=0;i<9;i++){
			int a=i/3,j=i%3;
			if(board[a][j]==0)
				return false;
		}
		return true;
	}
}
class XOButton extends JButton implements ActionListener{
	ImageIcon X,O;
	public XOButton(){
		X=new ImageIcon("/Users/atulkhetan/Desktop/X.png");
		O=new ImageIcon("/Users/atulkhetan/Desktop/O.png");
		this.addActionListener(this);
	}
	public void actionPerformed(ActionEvent e){
		JButton button = (JButton)e.getSource();
        String label= button.getText();
        int box = Integer.parseInt(label);
        if(BackEnd.isEmpty(box)){
        		byte value= BackEnd.player;
        		switch(value){
        		case 1:
        			setIcon(X);
        			break;
        		case 2:
        			setIcon(O);
        			break;
        		}
        		if(BackEnd.checkWin()){
        			JOptionPane.showMessageDialog(null, "Player : "+ value+" wins");
        			System.exit(0);
        		}
        		if(BackEnd.checkTie()){
        			JOptionPane.showMessageDialog(null,"The game was a tie");
        			System.exit(0);
        		}
        		BackEnd.setPlayer();
        }
	}
}
