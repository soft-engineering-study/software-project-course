package patterns.interpreter.smells;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ProductFinder {
	
	private ProductRepository repository;

	public ProductFinder(ProductRepository createProductRepository) {
		// TODO Auto-generated constructor stub
		this.repository = repository;
	}

	public List byColor(Color colorOfProductToFind) {
		List foundProducts = new ArrayList();
		Iterator<Product> products = null;
		while(products.hasNext()){
			Product product = (Product)products.next();
			if (product.getColor().equals(colorOfProductToFind)) {
				foundProducts.add(product);
			}
		}
		return foundProducts;
	}

	public List byPrice(double priceLimit) {
		List foundProducts = new ArrayList();
		Iterator<Product> products = null;
		while(products.hasNext()){
			Product product = (Product)products.next();
			if (product.getPrice() == priceLimit) {
				foundProducts.add(product);
			}
		}
		return foundProducts;
	}

	public List byColorSizeAndBelowPrice(Color color, ProductSize size, float price) {
		List foundProducts = new ArrayList();
		Iterator<Product> products = null;
		while(products.hasNext()){
			Product product = (Product)products.next();
			if (product.getColor() == color && 
				product.getSize() == size &&
				product.getPrice() < price) {
				foundProducts.add(product);
			}
		}
		return foundProducts;
	}

	public List belowPriceAvoidingAColor(float price, Color color) {
		List foundProducts = new ArrayList();
		Iterator<Product> products = null;
		while(products.hasNext()){
			Product product = (Product)products.next();
			if (product.getColor() != color &&
				product.getPrice() < price) {
				foundProducts.add(product);
			}
		}
		return foundProducts;
	}

}
