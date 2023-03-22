import java.io.IOException;
import java.util.Scanner;
import java.util.TreeSet;

class Example{

	public static Scanner txtreader;
	public static String[] positions = new String[]{"GK", "DF", "MF", "FW"};


	public static class Player{

		int pId, birthyear, height, weight;
		String position, name, surname;
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

	// public class PlayerComparator implements Comparator<Player>{
	// 	@Override
	// 	public int compare(Player p1, Player p2) {
	// 		if(p1.birthyear == p2.birthyear) return p1.pId - p2.pId;
	// 		return p1.birthyear - p2.birthyear;
	// 	}
		
	// }
	// PlayerComparator compar = new PlayerComparator();
	// TreeSet<Player> playerTree = new TreeSet<Player>(compar);

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
			// playerTree.add(pp);

		}
		txtreader.close();
	}



}