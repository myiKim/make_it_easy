import java.io.IOException;
import java.util.Scanner;
import java.util.TreeSet;
import java.util.Comparator;

class Player{

	int pId, birthyear, height, weight;
	String position, name, surname;
	String[] positions = new String[]{"GK", "DF", "MF", "FW"};

	Player(int pId, int birthyear, int height, int weight, int position, String name, String surname){
		this.pId = pId;
		this.birthyear = birthyear;
		this.height = height;
		this.weight = weight;
		this.position = positions[position];
		this.name = name;
		this.surname = surname;
	}

}



class Example{

	public static Scanner txtreader;
	
	public static Comparator<Player> compar= new Comparator<Player>(){
    	@Override
        public int compare(Player a , Player b){
    	    if(a.birthyear ==b.birthyear){

    			return a.pId-b.pId;
        	}
        	return a.birthyear - b.birthyear;
        }        
    };
	public static TreeSet<Player> playerTree = new TreeSet<Player>(compar);

	public static void main(String[] args) throws Exception{

		System.setIn(new java.io.FileInputStream("data/player_list.txt"));
		txtreader = new Scanner(System.in);


		final int NUM_PLAYERS = txtreader.nextInt();
		// read player data from txt file, and create an Player instance
		for(int i =0; i<NUM_PLAYERS; i++){
			int playerId = txtreader.nextInt();
			int playerBirthYear = txtreader.nextInt();
			int playerHeight = txtreader.nextInt();
			int playerWeight = txtreader.nextInt();
			int playerPosition = txtreader.nextInt();
			String playerName = txtreader.next();
			String playerSurname = txtreader.next();
			Player pp = new Player(playerId, playerBirthYear, playerHeight, playerWeight, playerPosition, playerName, playerSurname);
			// System.out.println(pp.height + "is player's height!");
			// System.out.println(pp.name + "<-- his name!");
			playerTree.add(pp);

		}
		
		while(true){
			Player popped = playerTree.pollFirst();

			if(popped == null) break;
			System.out.println("now popped a player!");
			System.out.println("Player ID:" + popped.pId);
			System.out.println("Player Name:" + popped.name);

		}

		txtreader.close();
	}



}