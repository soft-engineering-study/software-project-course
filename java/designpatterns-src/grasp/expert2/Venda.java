package br.ic.grasp.expert2;

import java.util.ArrayList;
import java.util.List;

public class Venda {
	
	List<ItemVenda> itens = new ArrayList<ItemVenda>();

	public double total() {
		double total = 0;
		
		boolean aplicarDesconto = false;
		
		if (itens.size() > 100) {
			aplicarDesconto = true;
		}
		
		for (ItemVenda itemVenda : itens) {
			EspecificacaoProduto especificacaoProduto = 
					itemVenda.getEspecificacaoProduto();
			double preco = especificacaoProduto.getPreco();
			
			if (aplicarDesconto) {
				preco = (1 - 
						especificacaoProduto.getPercentualDesconto()) * 
						preco;
			}
			
			double subtotal = itemVenda.getQuantidade()*preco;
			total+=subtotal;
		}
		
		return total;
	}
}
