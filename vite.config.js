import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
    build: {
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'index.html'),
                about: resolve(__dirname, 'about.html'),
                service: resolve(__dirname, 'service.html'),
                project: resolve(__dirname, 'project.html'),
                contact: resolve(__dirname, 'contact.html'),
                feature: resolve(__dirname, 'feature.html'),
                terms: resolve(__dirname, 'terms.html'),
                'index-en': resolve(__dirname, 'index-en.html'),
                'about-en': resolve(__dirname, 'about-en.html'),
                'service-en': resolve(__dirname, 'service-en.html'),
                'project-en': resolve(__dirname, 'project-en.html'),
                'contact-en': resolve(__dirname, 'contact-en.html'),
                'feature-en': resolve(__dirname, 'feature-en.html'),
                'terms-en': resolve(__dirname, 'terms-en.html'),
                404: resolve(__dirname, '404.html'),
                '404-en': resolve(__dirname, '404-en.html'),
            },
        },
    },
});
