import { Component, inject } from '@angular/core';
import { ProductListComponent } from './components/product-list/product-list.component';
import { ProductService } from './services/product.service';
import { Category } from './models/category.model';
import { Product } from './models/product.model';
import { CommonModule } from '@angular/common';
import { ProductCardComponent } from './components/product-card/product-card.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ProductListComponent, CommonModule, ProductCardComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  productService = inject(ProductService);

  categories: Category[] = this.productService.categories;

  allProducts: Product[] = this.productService.products;  
  products: Product[] = [];                             

  favorites: Product[] = [];

  categoryId: number | null = null;

  selectCategory(id: number) {
    this.categoryId = id;

    this.products = this.allProducts.filter(
      p => p.categoryId === id
    );
  }

  onDeleteProduct(id: number) {
    this.allProducts = this.allProducts.filter(p => p.id !== id);
    this.products = this.products.filter(p => p.id !== id);
    this.favorites = this.favorites.filter(p => p.id !== id);
  }

  toggleFavorite(productId: number): void {
    const product = this.allProducts.find(p => p.id === productId);
    if (!product) return;
    product.isFavorite = !product.isFavorite;
    this.favorites = this.allProducts.filter(p => p.isFavorite);
  }
}