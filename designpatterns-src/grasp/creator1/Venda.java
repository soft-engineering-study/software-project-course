package br.ic.grasp.creator1;
import java.util.ArrayList;
import java.util.List;

public class Venda {
	
	List<ItemVenda> itens;

	public double total() {
		double total = 0;
		
		boolean aplicarDesconto = false;
		
		if (itens.size() > 100) {
			for (ItemVenda itemVenda : itens) {
				total+=itemVenda.subtotalComDesconto();
			}
		}else{
			for (ItemVenda itemVenda : itens) {
				total+=itemVenda.subtotal();
			}
		}
		
		
		
		return total;
	}
	
	public ItemVenda criarItemVenda(int quantidade){
		ItemVenda itemVenda = new ItemVenda(quantidade);
		itens.add(itemVenda);
		return itemVenda;
	}
	
}
