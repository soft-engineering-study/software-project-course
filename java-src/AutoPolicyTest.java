
public class AutoPolicyTest {
    public static void main(String[] args) {
        // create two AutoPolicy objects
        AutoPolicy policy1 = new AutoPolicy(1111111, "Toyota Camry", "NJ");
        AutoPolicy policy2 = new AutoPolicy(2222222, "Toyota Fusion", "ME");

        // display whether each policy is in no-fault state
        policyInNoFaultState(policy1);
        policyInNoFaultState(policy2);
    }

    // this method displays whether an AutoPolicy
    // is in a state with no-fault auto insurance
    public static void policyInNoFaultState(AutoPolicy policy) {
        System.out.println("The auto policy: ");
        System.out.printf("Account #: %d; Car: %s; State %s %s a no-fault state%n%n",
                policy.getAccountNumber(), policy.getMakeAndModel(),
                policy.getState(),
                (policy.isNoFaultState() ? "is" : "is not"));
    }
}
