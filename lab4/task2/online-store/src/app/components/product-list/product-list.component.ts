import { Product } from '../../models/product.model';
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ProductCardComponent } from '../product-card/product-card.component';

@Component({
  selector: 'product-list',
  standalone: true,
  imports: [CommonModule, ProductCardComponent, FormsModule],
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css'],
})
export class ProductListComponent implements OnInit {
  searchQuery: string = '';
  filteredProducts: Product[] = [];

  products: Product[] = [
    {
      id: 112809322,
      name: 'Смартфон OPPO A78 8 ГБ/256 ГБ зеленый',
      description: 'OPPO A78 8 ГБ/256 ГБ — это стильный и производительный смартфон...',
      price: 109990,
      rating: 4.9,
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h07/hfb/83109614714910.jpg',
      images: ['https://resources.cdn-kaspi.kz/img/m/p/p4e/pab/64514776.png', 'https://resources.cdn-kaspi.kz/img/m/p/pf9/paa/64514779.png', 'https://resources.cdn-kaspi.kz/img/m/p/p8d/pa8/64514780.png'],
      link: 'https://kaspi.kz/shop/p/oppo-a78-8-gb-256-gb-zelenyi-112809322/'
    },
    {
      id: 101115165,
      name: 'Видеокарта GIGABYTE GeForce RTX 3060 GAMING OC 12GB',
      description: 'Система охлаждения WINDFORCE 3X...',
      price: 269990,
      rating: 4.8,
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h0f/h27/64026161971230.jpg',
      images: ['https://resources.cdn-kaspi.kz/img/m/p/hf2/h6e/64026167672862.jpg', 'https://resources.cdn-kaspi.kz/img/m/p/hb3/h27/64026171277342.jpg', 'https://resources.cdn-kaspi.kz/img/m/p/h63/h4a/64026164985886.jpg'],
      link: 'https://kaspi.kz/shop/p/gigabyte-geforce-rtx-3060-gaming-oc-12gb-101115165/'
    },
    {
      id: 104151899,
      name: 'Блок питания Deepcool PF550 R-PF550D-HA0B-EU 550 Вт',
      description: 'Блок питания Deepcool PF550...',
      price: 22990,
      rating: 4.8,
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h80/he9/86350817132574.png',
      images: ['https://resources.cdn-kaspi.kz/img/m/p/hab/h0b/86350817165342.jpg', 'https://resources.cdn-kaspi.kz/img/m/p/h27/hff/86350817198110.jpg', 'https://resources.cdn-kaspi.kz/img/m/p/h65/h70/86350817230878.jpg'],
      link: 'https://kaspi.kz/shop/p/deepcool-pf550-r-pf550d-ha0b-eu-550-vt-104151899/'
    },
    {
      id: 100956618,
      name: 'Мышь Logitech G102 Lightsync черный',
      description: 'Мышь проводная Logitech G102 LightSync...',
      price: 6998,
      rating: 4.9,
      image: 'https://resources.cdn-kaspi.kz/img/m/p/hb2/hc2/64119540187166.jpg',
      images: ['https://resources.cdn-kaspi.kz/img/m/p/pc7/p9b/105790332.jpeg', 'https://resources.cdn-kaspi.kz/img/m/p/ha5/h08/64119543070750.jpg', 'https://resources.cdn-kaspi.kz/img/m/p/h50/hea/64119545036830.jpg'],
      link: 'https://kaspi.kz/shop/p/logitech-g102-lightsync-chernyi-100956618/'
    },
    {
      id: 102073038,
      name: 'Ноутбук HP 15s 15.6" / 8 Гб / SSD 512 Гб / Win 10 / 15s-fq2074ur / 4A793EA',
      description: 'Занимайтесь важными делами сколько потребуется...',
      price: 298663,
      rating: 4.9,
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h08/he4/64217326780446.jpg',
      images: ['https://resources.cdn-kaspi.kz/img/m/p/h76/hf3/64217330614302.jpg', 'https://resources.cdn-kaspi.kz/img/m/p/h38/hdd/64217333825566.jpg', 'https://resources.cdn-kaspi.kz/img/m/p/hf6/hc8/64217336447006.jpg'],
      link: 'https://kaspi.kz/shop/p/hp-15s-15-6-8-gb-ssd-512-gb-win-10-15s-fq2074ur-4a793ea-102073038/'
    },
    {
      id: 140639712,
      name: 'Планшет Xiaomi Redmi Pad 2 11 дюйм 8 Гб/256 Гб серый',
      description: 'Xiaomi Redmi Pad 2 — универсальный планшет...',
      price: 107629,
      rating: 5,
      image: 'https://resources.cdn-kaspi.kz/img/m/p/pac/p7a/81439516.jpg',
      images: ['https://resources.cdn-kaspi.kz/img/m/p/p24/p44/46204507.png', 'https://resources.cdn-kaspi.kz/img/m/p/pec/p43/46204509.jpg', 'https://resources.cdn-kaspi.kz/img/m/p/p63/p41/46204511.png'],
      link: 'https://kaspi.kz/shop/p/xiaomi-redmi-pad-2-11-djuim-8-gb-256-gb-seryi-140639712/'
    },
    {
      id: 115974804,
      name: 'Микрофон K6 черный, желтый',
      description: 'Он - твой верный спутник в мире интервью и блогов...',
      price: 3577,
      rating: 4.2,
      image: 'https://resources.cdn-kaspi.kz/img/m/p/p14/p55/3940198.png',
      images: ['https://resources.cdn-kaspi.kz/img/m/p/p9c/p9f/3940203.png', 'https://resources.cdn-kaspi.kz/img/m/p/pd4/p9f/3940205.png', 'https://resources.cdn-kaspi.kz/img/m/p/pf1/p9f/3940206.png'],
      link: 'https://kaspi.kz/shop/p/mikrofon-k6-chernyi-zheltyi-115974804/'
    },
    {
      id: 149777154,
      name: 'Чехол для OPPO A78 серый',
      description: 'Чехол для OPPO A78 серый — это надёжная защита...',
      price: 898,
      rating: 4,
      image: 'assets/images/8_1.jpg',
      images: ['assets/images/8_2.jpg', 'assets/images/8_3.jpg', 'assets/images/8_4.jpg'],
      link: 'https://kaspi.kz/shop/p/chehol-dlja-oppo-a78-seryi-149777154/'
    },
    {
      id: 117690906,
      name: 'Смарт-часы Nepro100device Man QZ2 50 мм черный-черный',
      description: 'NEPRO100DEVICE Man QZ2 — это мужские умные часы...',
      price: 20890,
      rating: 4.9,
      image: 'assets/images/9_2.jpg',
      images: ['assets/images/9_3.jpg', 'assets/images/9_4.jpg'],
      link: 'https://kaspi.kz/shop/p/nepro100device-man-qz2-50-mm-chernyi-chernyi-117690906/'
    },
    {
      id: 143662037,
      name: 'Дрон AE AE60 Ultra черный',
      description: 'Квадрокоптер AE AE60 Ultra — высокотехнологичное устройство...',
      price: 249990,
      rating: 4.9,
      image: 'assets/images/10_1.jpeg',
      images: ['assets/images/10_2.jpeg', 'assets/images/10_3.jpeg', 'assets/images/10_4.jpeg'],
      link: 'https://kaspi.kz/shop/p/nepro100device-man-qz2-50-mm-chernyi-chernyi-117690906/'
    }
  ];

  ngOnInit() {
    this.filteredProducts = this.products;
  }

  filterProducts(): void {
    const query = this.searchQuery.toLowerCase();
    this.filteredProducts = this.products.filter(product =>
      product.name.toLowerCase().includes(query)
    );
  }
}