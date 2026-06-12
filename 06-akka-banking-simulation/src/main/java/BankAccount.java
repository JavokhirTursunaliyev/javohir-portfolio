import akka.actor.AbstractActor;

public class BankAccount extends AbstractActor {
    private int balance = 100;

    @Override
    public void preStart() {
        System.out.println("Initial balance: £" + balance);
    }

    @Override
    public Receive createReceive() {
        return receiveBuilder()
                .match(Deposit.class, deposit -> {
                    balance += deposit.getAmount();
                    System.out.println("Deposited £" + deposit.getAmount() + " | New Balance: £" + balance);
                })
                .match(Withdrawal.class, withdrawal -> {
                    balance += withdrawal.getAmount(); // Amount is negative
                    System.out.println("Withdrew £" + Math.abs(withdrawal.getAmount()) + " | New Balance: £" + balance);
                })
                .build();
    }
}
