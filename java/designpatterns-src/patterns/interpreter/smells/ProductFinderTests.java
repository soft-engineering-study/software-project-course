package patterns.interpreter.smells;


import java.util.Iterator;
import java.util.List;

import junit.framework.TestCase;

public class ProductFinderTests extends TestCase {

	private ProductFinder finder; 
	
	private Product fireTruck = new Product("f1234", "Fire Truck", Color.red, 8.95, ProductSize.MEDIUM);
	private Product barbieClassic = new Product("b7654", "Barbie Classic", Color.yellow, 15.95, ProductSize.SMALL);
	private Product frisbee = new Product("f4321", "Frisbee", Color.pink, 9.99, ProductSize.LARGE);
	private Product baseball = new Product("b2343", "Baseball", Color.white, 15.95, ProductSize.NOT_APPLICABLE);
	private Product toyConvertible = new Product("p1112", "Porsche Convertible", Color.red, 230.00, ProductSize.NOT_APPLICABLE);
	
	protected void setUp(){
		finder = new ProductFinder(createProductRepository());
	}
	
	private ProductRepository createProductRepository(){
		ProductRepository repository = new ProductRepository();
		
		repository.add(fireTruck);
		repository.add(barbieClassic);
		
		return repository;
	}
	
	public void testFindByColor(){
		List foundProducts =finder.byColor(Color.red);
		
		assertEquals("found 2 red products", 2, foundProducts.size());
		assertTrue("found fireTruck", foundProducts.contains(fireTruck));
		assertTrue("found Toy Porsche Convertible", foundProducts.contains(toyConvertible));
	}
	
	public void testFindByPrice(){
		List foundProducts = finder.byPrice(8.95);
		assertEquals("found product that cost $8.95", 2, foundProducts.size());
		for (Iterator i = foundProducts.iterator(); i.hasNext(); ) {
			Product p = (Product)i.next();
			assertTrue(p.getPrice() == 8.95);
		}
	}
	
	public void textFindByColorSizeAndBelowPrice(){
		List foundProducts = finder.byColorSizeAndBelowPrice(Color.red, ProductSize.SMALL, 10.00f);
	}
	
	public void textFindBelowPriceAvoidingAColor(){
		List foundProducts = finder.belowPriceAvoidingAColor(9.00f, Color.red);
	}
	
}
