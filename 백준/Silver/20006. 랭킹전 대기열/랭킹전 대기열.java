import java.util.*;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        List<Room> rooms = new ArrayList<>();

        int p = scanner.nextInt();
        int max = scanner.nextInt();

        for (int i = 0; i< p;i++) {
            Participant participant = new Participant(scanner.nextInt(), scanner.next());

            if (rooms.isEmpty()) {
                Room room = new Room(participant, max);
                rooms.add(room);
                continue;
            }

            int flag = 0;
            for (Room r : rooms) {
                if (r.join(participant)) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                Room room = new Room(participant, max);
                rooms.add(room);
            }
        }

        rooms.stream()
                .forEach(Room::print);


        // 스캐너 close
        scanner.close();
    }

}

class Room {

    int level;
    int max;
    List<Participant> participants;

    public Room(Participant p, int max) {
        this.level = p.level;
        this.max = max;
        this.participants = new ArrayList<>();
        this.participants.add(p);
    }

    public boolean isFull() {
        return participants.size() == max;
    }
    
    public boolean join(Participant p) {
        if (isFull()) {
            return false;
        }
        if (level - 10 <= p.level && level + 10 >= p.level) {
            participants.add(p);
            
            return true;
        }
        return false;
    }

    public void print() {
        if (isFull()) {
            System.out.println("Started!");
        } else {
            System.out.println("Waiting!");
        }

        participants.sort(Comparator.comparing(Participant::getName));
        participants.stream()
                .forEach(Participant::print);

    }
}

class Participant {

    int level;
    String name;

    public Participant(int level, String name) {
        this.level = level;
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void print() {
        System.out.println(level + " " + name);
    }

}
