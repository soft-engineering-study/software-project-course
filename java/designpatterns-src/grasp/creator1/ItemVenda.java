package br.ic.grasp.creator1;
import br.ic.grasp.expert2.*;


public class ItemVenda {

	private EspecificacaoProduto especificacaoProduto = new EspecificacaoProduto();
	private int quantidade = 0;
	
	public ItemVenda(int quantidade) {
		// TODO Auto-generated constructor stub
		this.quantidade = quantidade;
	}

	public EspecificacaoProduto getEspecificacaoProduto() {
		return especificacaoProduto;
	}
	
	public int getQuantidade() {
		return quantidade;
	}

	public double subtotalComDesconto() {
		// TODO Auto-generated method stub
		double preco = especificacaoProduto.getPreco();
		
		preco = (1 - especificacaoProduto.getPercentualDesconto()) * preco;
		
		double subtotalComDesconto = getQuantidade()*preco;
		return subtotalComDesconto;
	}

	public double subtotal() {
		// TODO Auto-generated method stub
		double preco = especificacaoProduto.getPreco();
		
		double subtotal = getQuantidade()*preco;
		return subtotal;
	}
}
