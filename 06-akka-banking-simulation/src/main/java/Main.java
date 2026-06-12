import akka.actor.ActorRef;
import akka.actor.ActorSystem;
import akka.actor.Props;

import java.util.Random;
import java.util.concurrent.TimeUnit;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        ActorSystem system = ActorSystem.create("BankSystem");
        ActorRef bankAccount = system.actorOf(Props.create(BankAccount.class), "bankAccount");

        Random rand = new Random();

        for (int i = 0; i < 10; i++) {
            int amount = rand.nextInt(2001) - 1000; // Range -1000 to +1000

            if (amount > 0) {
                bankAccount.tell(new Deposit(amount), ActorRef.noSender());
            } else {
                bankAccount.tell(new Withdrawal(amount), ActorRef.noSender());
            }

            TimeUnit.MILLISECONDS.sleep(500); // Optional: delay for readability
        }

        // Allow processing before shutdown
        Thread.sleep(3000);
        system.terminate();
    }
}
