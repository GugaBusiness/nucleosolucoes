# Mapa Completo do Site - Dr. João Assaf (drjoaoassaf.com.br)

Este documento foi gerado de forma minuciosa para servir de mapeamento completo de toda a estrutura do site (seções, textos, links, fluxos de popup e botões de ação) e do inventário completo de arquivos contidos na pasta `assets`, detalhando onde e como cada um deles é referenciado ou linkado no código fonte do arquivo principal `index.html`.

---

## 1. Informações Gerais e SEO
- **Título da Página (`<title>`):** `Dr João Assaf – Cirurgia Plástica em Bauru e Alphaville`
- **Idioma do Documento:** `pt-BR` (Português - Brasil)
- **Meta Robots:** `max-image-preview:large`
- **Gerador:** WordPress 6.9.4 & Elementor 4.0.7
- **Responsividade:** Configurado com viewport adaptativo para dispositivos móveis (`width=device-width, initial-scale=1.0, viewport-fit=cover`).
- **Verificação do Google:** `GVDZ7tdiefj-fD_HiweshgFMawd7EJwvjuJUPcacBWA`

---

## 2. Estrutura de Seções e Conteúdo do Site (`index.html`)
A página principal é uma Landing Page estruturada em seções construídas via Elementor, identificadas por IDs de âncoras para navegação suave. Abaixo está o mapeamento detalhado de cada seção em ordem de aparecimento:

### 2.1. Cabeçalho / Menu de Navegação (Header)
*   **Container HTML:** Div de classe `elementor-element-11cbc95e` (com animação `fadeInDown`).
*   **Logo Principal:**
    *   Imagem principal: `assets/images/002144c88d9d745e_k2.png` (766px de largura).
    *   Imagem responsiva (srcset): `assets/images/b0fdf819035997e7_k2-300x112.png` (300px de largura).
    *   Âncora do Logo: Aponta para `#inicio` (topo da página).
*   **Menu de Navegação Desktop & Mobile:**
    *   Classe de estilo: `elementor-widget-nav-menu` (Widget ID: `02f5daa`).
    *   **Itens do Menu e Links de Âncora:**
        1.  **Sobre:** Aponta para `#sobre`
        2.  **Soluções:** Aponta para `#solucoes`
        3.  **Para quem é:** Aponta para `#para-quem-e`
        4.  **Depoimentos:** Aponta para `#depoimentos`
        5.  **Dúvidas:** Aponta para `#faq`
        6.  **Contato:** Aponta para `#contato`

### 2.2. Seção Hero / Introdução (`#inicio`)
*   **ID do Container:** `inicio` (Widget ID: `5b543cd3`).
*   **Conteúdo Textual:**
    *   **Título Principal (H2):**
        > Dr. João Assaf
        > Cirurgia Plástica em Bauru - SP e Alphaville - SP
    *   **Subtexto de Apoio:**
        > Transformando vidas através de uma cirurgia plástica ética, segura e com resultados naturais. Excelência técnica e atendimento humanizado para o seu bem-estar.
*   **Botão de Ação Principal:**
    *   **Texto:** `Agendar consulta` (com ícone do WhatsApp).
    *   **Ação:** Abre o **Popup de Seleção de Local (ID 80)** via link codificado do Elementor:
        `#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjgwIiwidG9nZ2xlIjpmYWxzZX0%3D` (Base64 decodificado como `{"id":"80","toggle":false}`).
*   **Diferenciais rápidos (Cards inferiores de destaque - Icon Boxes):**
    *   **Diferencial 1:** `Atendimentos presenciais em Alphaville, Barueri e Bauru (SP)` (Ícone SVG personalizado).
    *   **Diferencial 2:** `Consultas Online e Presenciais` (Ícone SVG personalizado).
    *   **Diferencial 3:** `Cirurgias em ambiente hospitalar de alta segurança` (Ícone SVG personalizado).

### 2.3. Seção Sobre (`#sobre`)
*   **ID do Container:** `sobre` (Widget ID: `5cc669af`).
*   **Foto do Dr. João Assaf:**
    *   Caminho local da imagem: `assets/images/a7e66f489554c46e_cp1-1.jpg` (Largura original: 800px).
    *   Imagens de resolução responsiva (srcset):
        *   `assets/images/0b86f3c3d3f05829_cp1-1-300x300.jpg` (300w)
        *   `assets/images/7890d910acad9a7a_cp1-1-150x150.jpg` (150w)
        *   `assets/images/6d34d4723a7b9c12_cp1-1-768x768.jpg` (768w)
*   **Conteúdo Textual:**
    *   **Título Principal (H2):** `Ciência, Arte e Segurança na sua Jornada de Transformação`
    *   **Registro Profissional:** `CRM-SP 155733 | RQE 87550`
    *   **Biografia/Descrição de Apoio:**
        > Com uma trajetória pautada pela ética e pelo aperfeiçoamento constante, o Dr. João Assaf dedica sua carreira a proporcionar resultados que respeitam a individualidade de cada paciente. Especialista em Cirurgia Plástica, sua abordagem une o rigor técnico à sensibilidade estética, garantindo que cada procedimento seja um passo em direção à sua melhor versão.
    *   **Destaques em tópicos:**
        *   Membro Especialista da Sociedade Brasileira de Cirurgia Plástica.
        *   Experiência em procedimentos de alta complexidade.
        *   Foco total na segurança do paciente e no pós-operatório assistido.

### 2.4. Seção Soluções (`#solucoes`)
*   **ID do Container:** `solucoes` (Widget ID: `2dff6961`).
*   **Título da Seção (H2):** `Soluções Personalizadas para sua Saúde e Autoestima`
*   **Procedimentos / Soluções (Apresentados em formato de container com efeito de rolagem sticky lateral):**
    1.  **Contorno Corporal (Lipoaspiração e Lipo HD):**
        *   Imagem: `assets/images/b73bed2137e1c03b_e0.jpg`
        *   Srcset responsivo: `assets/images/55c4c1ddbfdfba63_e0-300x229.jpg`, `assets/images/d3ecb8e8e107716f_e0-1024x783.jpg`, `assets/images/18c893d180c26748_e0-768x587.jpg`.
        *   Descrição: *Recupere a harmonia das suas curvas com tecnologias que removem a gordura localizada e definem o contorno muscular com precisão.*
    2.  **Abdominoplastia:**
        *   Imagem: `assets/images/0bb248be7bf5d50d_e1.jpg`
        *   Srcset responsivo: `assets/images/6f7de7e6882d5555_e1-300x229.jpg`, `assets/images/9ba5c1fe370f6673_e1-1024x783.jpg`, `assets/images/46db8e4c2a0f9c3c_e1-768x587.jpg`.
        *   Descrição: *Diga adeus à flacidez abdominal e ao “abdômen caído”. Um procedimento focado em devolver a firmeza e a confiança ao seu corpo.*
    3.  **Técnica de preservação de tecidos mamários:**
        *   Imagem: `assets/images/7261da7609df9009_e2.jpg`
        *   Srcset responsivo: `assets/images/bf0e6b2a17965b1c_e2-300x229.jpg`, `assets/images/abc1074c4238e7f2_e2-1024x783.jpg`, `assets/images/d3a3157b0ecafc6e_e2-768x587.jpg`.
        *   Descrição: *PRESERVÉ: Uma recuperação operatória ultra rápida, baseada em uma técnica que preserva ao máximo os tecidos mamários, reduzindo traumas cirúrgicos e favorecendo um pós-operatório mais confortável, com retorno mais ágil às atividades e resultados mais naturais.*
    4.  **Procedimentos Faciais:**
        *   Imagem: `assets/images/5b0efacd9ac868d6_e3.jpg`
        *   Srcset responsivo: `assets/images/08a1a6dcc9223440_e3-300x229.jpg`, `assets/images/79e46b4922bafcb5_e3-1024x783.jpg`, `assets/images/07f5de8f20b55571_e3-768x587.jpg`.
        *   Descrição: *Rejuvenescimento natural para realçar sua beleza sem perder sua essência.*
*   **Botão de Ação da Seção (Widget `74c2ecc0`):**
    *   **Texto:** `Agendar minha consulta` (Ícone do WhatsApp).
    *   **Ação:** Abre o **Popup de Seleção de Local (ID 80)** via link de popup do Elementor.

### 2.5. Seção Para Quem É (`#para-quem-e`)
*   **ID do Container:** `para-quem-e` (Widget ID: `25a4dfff`).
*   **Título Principal (H2):** `Este é o momento ideal para você se...`
*   **Cards de Perfil do Paciente (Icon Boxes):**
    *   **Card 1:** `Você sente que a flacidez abdominal ou mamária afeta sua autoestima e escolha de roupas.` (Ícone de cabide/vestuário).
    *   **Card 2:** `Você busca um profissional que prioriza a segurança e a transparência em cada etapa.` (Ícone de escudo/médico).
    *   **Card 3:** `Você deseja um resultado natural, elegante e que respeite sua anatomia.` (Ícone de harmonia corporal).
    *   **Card 4:** `Você valoriza um atendimento individualizado, do pré ao pós-operatório.` (Ícone de suporte/atendimento).
*   **Botão de Ação da Seção (Widget `70506234`):**
    *   **Texto:** `Agendar consulta` (Ícone do WhatsApp).
    *   **Ação:** Abre o **Popup de Seleção de Local (ID 80)** via link de popup do Elementor.

### 2.6. Seção Depoimentos (`#depoimentos`)
*   **ID do Container:** `depoimentos` (Widget ID: `2c8da293`).
*   **Título Principal (H2):** `Depoimentos`
*   **Widget Widget de Depoimentos do Google (Trustindex):**
    *   Renderizado dinamicamente via shortcode na div:
        `<div data-css-url="https://drjoaoassaf.com.br/wp-content/uploads/trustindex-google-widget.css?1773252711" data-src="https://cdn.trustindex.io/loader.js?wp-widget" data-ti-widget-inited="true"></div>`
    *   O script que alimenta este widget é o `assets/js/0eb0f6be05ca6315_loader.js`.

### 2.7. Seção Dúvidas Frequentes (`#faq`)
*   **ID do Container:** `faq` (Widget ID: `21bc207f`).
*   **Título Principal (H2):** `Dúvidas frequentes`
*   **Sanfona Accordion (Widget `489c7d34`):**
    *   Usa elementos HTML5 semânticos `<details>` e `<summary>` para expansão nativa.
    *   **Perguntas e Respostas:**
        1.  **Onde são realizadas as cirurgias?**
            > Todas as cirurgias são realizadas em hospitais de referência em Alphaville, São Paulo e Bauru, equipados com UTI e toda a estrutura necessária para sua segurança.
        2.  **Como funciona a recuperação?**
            > Cada paciente recebe um protocolo de recuperação personalizado, com acompanhamento próximo da nossa equipe para garantir o melhor resultado final.
        3.  **O Dr. João Assaf atende convênios?**
            > Nossos atendimentos são focados em consultas particulares, garantindo o tempo e a dedicação necessários para um planejamento cirúrgico de excelência.

### 2.8. Rodapé (Contato / Footer) (`#contato`)
*   **ID do Container:** `contato` (Widget ID: `56f0d447`).
*   **Chamada para Ação:** `Inicie sua jornada hoje mesmo`
    *   Botão: `Agendar consulta` (Abre o popup 80).
*   **Lista de Informações de Contato (Colunas Esquerda e Direita):**
    *   **WhatsApp:** Link que abre o Popup de Local 80.
    *   **Endereço:** `Alphaville - SP | Bauru - SP` -> Aponta para o link externo do Google Maps: `https://maps.app.goo.gl/n4C8LuDLLNGK9FS89`.
    *   **Instagram:** `@dr.joaoassaf` -> Aponta para: `https://www.instagram.com/dr.joaoassaf/`.
*   **Mapa Interativo Embutido (Iframe):**
    *   Aponta para o endereço do Dr. João Assaf no Google Maps em Bauru, SP.
    *   Caminho local do mapa embutido: `assets/documents/623ed884ea36c099_maps.html`.
*   **Logo de Rodapé:**
    *   Imagem principal: `assets/images/5727775ef2373966_k1.png`
    *   Srcset responsivo: `assets/images/cea402a1c2a8ee9a_k1-300x112.png`
*   **Menu do Rodapé:**
    *   Replicado verticalmente com links diretos para as seções `#sobre`, `#solucoes`, `#para-quem-e`, `#depoimentos`, `#faq`, `#contato`.
*   **Copyright:** `Copyright © 2026 Dr. João Assaf. Todos os direitos reservados.`
*   **Desenvolvedor do Site:** `Feito por LDT Assessoria` -> Link externo aponta para `http://www.ldtassessoria.com.br/` (Espelhado localmente no asset `assets/documents/df96b950b87ffb96_file.html`).
*   **Botão Flutuante Permanente do WhatsApp:**
    *   Posicionado de forma fixa na tela (`elementor-fixed`).
    *   Ação: Clicar nele abre o Popup de Seleção de Local (ID 80).


---

## 3. Fluxo de Botões de Ação e o Popup de Seleção de Local (ID 80)
Todos os botões principais de agendamento no site não abrem um WhatsApp diretamente, mas sim um modal de escolha de local. Este modal é controlado pelo script e folhas de estilos do Elementor:

- **Gatilho de Abertura:** Qualquer elemento com o atributo `href` igual a `#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjgwIiwidG9nZ2xlIjpmYWxzZX0%3D`.
- **Identificação do Elemento:** O modal se insere sob o ID `#elementor-popup-modal-80` com a classe `.elementor-80`.
- **Estilos do Modal:** Definidos no arquivo `assets/css/45f0231564a9cfe9_post-80.css`.
- **Estrutura Interna do Popup (encontrada no mapeamento de backup):**
  - **Título:** `Escolha o local para atendimento:`
  - **Botão 1 (São Paulo):**
    - **Rótulo:** `Agendar em São Paulo` (ID do Widget: `1d797ee`)
    - **Link de Destino:** `https://tintim.link/whatsapp/cd258c7d-a0c8-488a-b293-957c255314b7/c060c1f8-93a7-4d53-be28-d6efa1d03527` (redirecionador inteligente)
  - **Botão 2 (Bauru):**
    - **Rótulo:** `Agendar em Bauru` (ID do Widget: `3088378`)
    - **Link de Destino:** `https://tintim.link/whatsapp/cd258c7d-a0c8-488a-b293-957c255314b7/94f35534-8f98-49a3-9c0e-c037d8c78a7c` (redirecionador inteligente)

---

## 4. Mapeamento de Dependências e Arquivos de Assets
O site possui **120 arquivos** locais em sua pasta `/assets`. A tabela abaixo categoriza cada um deles, ligando-os ao seu respectivo propósito, a URL original da web e sua exata utilização no código do `index.html`.

### 4.31 HTML Document / Backup
| Arquivo em /assets | URL Original | Utilização / Links em index.html |
| --- | --- | --- |
| `1ebd95fa6270b1df_GetPlace` | `https://places.googleapis.com/$rpc/google.maps.places.v1.Places/GetPlace` | Mapeado para resolução offline (Linha 57) |
| `2ef2e449385eb70a_xmlrpc.php` | `https://drjoaoassaf.com.br/xmlrpc.php?rsd` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 225 no trecho: `<link href="assets/json/ef2e20f4016628ff_file.json" rel="https://api.w.org/"/><link h...` |
| `473fcc30346e5f7d_font.html` | `https://fonts.gstatic.com/l/font?kit=5aUu9-KzpRiLCAt4Unrc-xIKmCU5mEh8jGdDgR9YgwwfxvM5NmKBR3I&skey=b20c8ebc9802c116&v=v25` | Mapeado para resolução offline (Linha 57) |
| `557500d6ab7d64d0_GetViewportInfo` | `https://maps.googleapis.com/$rpc/google.internal.maps.mapsjs.v1.MapsJsInternalService/GetViewportInfo` | Mapeado para resolução offline (Linha 57) |
| `55d56d622d3aa5c3_file` | `https://drjoaoassaf.com.br/feed/` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 176 no trecho: `<link href="assets/documents/55d56d622d3aa5c3_file" rel="alternate" title="Feed para Dr Jo...` |
| `59340bd23c35dc7a_GetPlaceWidgetMetadata` | `https://maps.googleapis.com/$rpc/google.internal.maps.mapsjs.v1.MapsJsInternalService/GetPlaceWidgetMetadata` | Mapeado para resolução offline (Linha 57) |
| `5a922de40fc58773_file` | `https://drjoaoassaf.com.br/comments/feed/` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 177 no trecho: `<link href="assets/documents/5a922de40fc58773_file" rel="alternate" title="Feed de comentá...` |
| `623ed884ea36c099_maps.html` | `https://maps.google.com/maps?q=Dr.%20Jo%C3%A3o%20Assaf%20%7C%20Cirurgi%C3%A3o%20pl%C3%A1stico.%20Cirurgi%C3%A3o%20pl%C3%A1stico%20em%20Bauru%2C%20S%C3%A3o%20Paulo&t=m&z=15&output=embed&iwloc=near` | Mapeado para resolução offline (Linha 57) |
| `882904a37fe37ab6_n4C8LuDLLNGK9FS89.html` | `https://maps.app.goo.gl/n4C8LuDLLNGK9FS89` | Mapeado para resolução offline (Linha 57) |
| `9a7fea20aeaea565_embed` | `https://drjoaoassaf.com.br/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fdrjoaoassaf.com.br%2F&format=xml` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 179 no trecho: `<link href="assets/documents/9a7fea20aeaea565_embed" rel="alternate" title="oEmbed (XML)" ...` |
| `d59d037cb02a6de9_InitMapsJwt` | `https://maps.googleapis.com/$rpc/google.internal.maps.mapsjs.v1.MapsJsInternalService/InitMapsJwt` | Mapeado para resolução offline (Linha 57) |
| `df96b950b87ffb96_file.html` | `http://www.ldtassessoria.com.br/` | Mapeado para resolução offline (Linha 57) |
| `f11e27616f375a9a_embed.html` | `https://www.google.com/maps/embed?origin=mfe&pb=!1m4!2m1!1sDr.+Jo%C3%A3o+Assaf+%7C+Cirurgi%C3%A3o+pl%C3%A1stico.+Cirurgi%C3%A3o+pl%C3%A1stico+em+Bauru,+S%C3%A3o+Paulo!5e0!6i15` | Mapeado para resolução offline (Linha 57) |
| `f886ec07b5850029_file.html` | `https://drjoaoassaf.com.br/` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 227 no trecho: `<link href="assets/documents/f886ec07b5850029_file.html" rel="canonical"/>...`<br>Linkado na linha 228 no trecho: `<link href="assets/documents/f886ec07b5850029_file.html" rel="shortlink"/>...` |

### 4.48 Image / Icon
| Arquivo em /assets | URL Original | Utilização / Links em index.html |
| --- | --- | --- |
| `002144c88d9d745e_k2.png` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/k2.png` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 330 no trecho: `<img alt="" class="attachment-large size-large wp-image-17" decoding="async" fet...` |
| `00420fb7d0cdd1a9_vt.jpg` | `https://www.google.com/maps/vt?pb=!1m5!1m4!1i12!2i1489!3i2308!4i256!2m1!1e1!3m12!2sen-US!3sUS!5e289!12m3!1e37!2m1!1ssmartmaps!12m4!1e26!2m2!1sstyles!2zcy5lOmx8cC52Om9mZg!4e0!5m1!1e3!23i47083502&key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&token=37733` | Mapeado para resolução offline (Linha 57) |
| `06f83c1607d3e35e_vt.webp` | `https://www.google.com/maps/vt?pb=!1m5!1m4!1i15!2i11917!3i18470!4i256!2m3!1e0!2sm!3i780544532!2m3!1e2!2sspotlit!5i1!3m13!2sen-US!3sUS!5e289!12m5!1e68!2m2!1sset!2sRoadmap!4e2!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!1e3!23i47083502!27m14!299174093m13!14m12!1m8!1m2!1y10718399135906546655!2y11839512752135877627!2s%2Fg%2F11qptkccp0!4m2!1x4071552626!2x3804343533!15sgcid%3Aplastic_surgeon!2b0!6b0!8b0&key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&token=67292` | Mapeado para resolução offline (Linha 57) |
| `07cb7ae82e1b1091_3k1-e1773410072734-150x150.png` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/3k1-e1773410072734-150x150.png` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 249 no trecho: `<link href="assets/images/07cb7ae82e1b1091_3k1-e1773410072734-150x150.png" rel="icon" s...` |
| `07f5de8f20b55571_e3-768x587.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e3-768x587.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 475 no trecho: `<img alt="" class="attachment-full size-full wp-image-24" decoding="async" heigh...` |
| `08a1a6dcc9223440_e3-300x229.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e3-300x229.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 475 no trecho: `<img alt="" class="attachment-full size-full wp-image-24" decoding="async" heigh...` |
| `08afd687c6a49fe3_vt.webp` | `https://www.google.com/maps/vt?pb=!1m5!1m4!1i15!2i11919!3i18471!4i256!2m3!1e0!2sm!3i780544532!2m3!1e2!2sspotlit!5i1!3m13!2sen-US!3sUS!5e289!12m5!1e68!2m2!1sset!2sRoadmap!4e2!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!1e3!23i47083502!27m14!299174093m13!14m12!1m8!1m2!1y10718399135906546655!2y11839512752135877627!2s%2Fg%2F11qptkccp0!4m2!1x4071552626!2x3804343533!15sgcid%3Aplastic_surgeon!2b0!6b0!8b0&key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&token=130598` | Mapeado para resolução offline (Linha 57) |
| `0b86f3c3d3f05829_cp1-1-300x300.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/cp1-1-300x300.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 421 no trecho: `<img alt="" class="attachment-large size-large wp-image-20" decoding="async" hei...` |
| `0bb248be7bf5d50d_e1.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e1.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 451 no trecho: `<img alt="" class="attachment-full size-full wp-image-22" decoding="async" heigh...` |
| `177edd439d5bffe3_vt.webp` | `https://www.google.com/maps/vt?pb=!1m5!1m4!1i15!2i11919!3i18470!4i256!2m3!1e0!2sm!3i780544532!2m3!1e2!2sspotlit!5i1!3m13!2sen-US!3sUS!5e289!12m5!1e68!2m2!1sset!2sRoadmap!4e2!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!1e3!23i47083502!27m14!299174093m13!14m12!1m8!1m2!1y10718399135906546655!2y11839512752135877627!2s%2Fg%2F11qptkccp0!4m2!1x4071552626!2x3804343533!15sgcid%3Aplastic_surgeon!2b0!6b0!8b0&key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&token=6119` | Mapeado para resolução offline (Linha 57) |
| `18c893d180c26748_e0-768x587.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e0-768x587.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 439 no trecho: `<img alt="" class="attachment-full size-full wp-image-21" decoding="async" heigh...` |
| `3b506326dfdfd5d0_vt.webp` | `https://www.google.com/maps/vt?pb=!1m5!1m4!1i15!2i11920!3i18471!4i256!2m3!1e0!2sm!3i780544532!2m3!1e2!2sspotlit!5i1!3m13!2sen-US!3sUS!5e289!12m5!1e68!2m2!1sset!2sRoadmap!4e2!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!1e3!23i47083502!27m14!299174093m13!14m12!1m8!1m2!1y10718399135906546655!2y11839512752135877627!2s%2Fg%2F11qptkccp0!4m2!1x4071552626!2x3804343533!15sgcid%3Aplastic_surgeon!2b0!6b0!8b0&key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&token=81289` | Mapeado para resolução offline (Linha 57) |
| `46db8e4c2a0f9c3c_e1-768x587.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e1-768x587.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 451 no trecho: `<img alt="" class="attachment-full size-full wp-image-22" decoding="async" heigh...` |
| `4a1fd74eb042ec9a_vt.webp` | `https://www.google.com/maps/vt?pb=!1m5!1m4!1i15!2i11918!3i18470!4i256!2m3!1e0!2sm!3i780544532!2m3!1e2!2sspotlit!5i1!3m13!2sen-US!3sUS!5e289!12m5!1e68!2m2!1sset!2sRoadmap!4e2!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!1e3!23i47083502!27m14!299174093m13!14m12!1m8!1m2!1y10718399135906546655!2y11839512752135877627!2s%2Fg%2F11qptkccp0!4m2!1x4071552626!2x3804343533!15sgcid%3Aplastic_surgeon!2b0!6b0!8b0&key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&token=102241` | Mapeado para resolução offline (Linha 57) |
| `55c4c1ddbfdfba63_e0-300x229.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e0-300x229.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 439 no trecho: `<img alt="" class="attachment-full size-full wp-image-21" decoding="async" heigh...` |
| `5727775ef2373966_k1.png` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/k1.png` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 686 no trecho: `<img alt="" class="attachment-large size-large wp-image-26" decoding="async" hei...` |
| `5b0efacd9ac868d6_e3.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e3.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 475 no trecho: `<img alt="" class="attachment-full size-full wp-image-24" decoding="async" heigh...` |
| `622c1db6848cb1f5_3k1-e1773410072734.png` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/3k1-e1773410072734.png` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 250 no trecho: `<link href="assets/images/622c1db6848cb1f5_3k1-e1773410072734.png" rel="icon" sizes="19...`<br>Linkado na linha 251 no trecho: `<link href="assets/images/622c1db6848cb1f5_3k1-e1773410072734.png" rel="apple-touch-ico...` |
| `6d34d4723a7b9c12_cp1-1-768x768.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/cp1-1-768x768.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 421 no trecho: `<img alt="" class="attachment-large size-large wp-image-20" decoding="async" hei...` |
| `6f7de7e6882d5555_e1-300x229.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e1-300x229.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 451 no trecho: `<img alt="" class="attachment-full size-full wp-image-22" decoding="async" heigh...` |
| `7261da7609df9009_e2.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e2.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 463 no trecho: `<img alt="" class="attachment-full size-full wp-image-23" decoding="async" heigh...` |
| `7342f390b12f636d_openhand_8_8.cur` | `https://maps.gstatic.com/mapfiles/openhand_8_8.cur` | Mapeado para resolução offline (Linha 57) |
| `741318befe413b0f_vt.webp` | `https://www.google.com/maps/vt?pb=!1m5!1m4!1i15!2i11920!3i18470!4i256!2m3!1e0!2sm!3i780544532!2m3!1e2!2sspotlit!5i1!3m13!2sen-US!3sUS!5e289!12m5!1e68!2m2!1sset!2sRoadmap!4e2!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!1e3!23i47083502!27m14!299174093m13!14m12!1m8!1m2!1y10718399135906546655!2y11839512752135877627!2s%2Fg%2F11qptkccp0!4m2!1x4071552626!2x3804343533!15sgcid%3Aplastic_surgeon!2b0!6b0!8b0&key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&token=87881` | Mapeado para resolução offline (Linha 57) |
| `7890d910acad9a7a_cp1-1-150x150.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/cp1-1-150x150.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 421 no trecho: `<img alt="" class="attachment-large size-large wp-image-20" decoding="async" hei...` |
| `79e46b4922bafcb5_e3-1024x783.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e3-1024x783.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 475 no trecho: `<img alt="" class="attachment-full size-full wp-image-24" decoding="async" heigh...` |
| `83507f25bc110f54_vt.webp` | `https://www.google.com/maps/vt?pb=!1m5!1m4!1i15!2i11916!3i18471!4i256!2m3!1e0!2sm!3i780544532!2m3!1e2!2sspotlit!5i1!3m13!2sen-US!3sUS!5e289!12m5!1e68!2m2!1sset!2sRoadmap!4e2!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!1e3!23i47083502!27m14!299174093m13!14m12!1m8!1m2!1y10718399135906546655!2y11839512752135877627!2s%2Fg%2F11qptkccp0!4m2!1x4071552626!2x3804343533!15sgcid%3Aplastic_surgeon!2b0!6b0!8b0&key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&token=25751` | Mapeado para resolução offline (Linha 57) |
| `94603dd27405ee73_cp1.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/cp1.jpg` | Mapeado para resolução offline (Linha 57) |
| `9ba5c1fe370f6673_e1-1024x783.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e1-1024x783.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 451 no trecho: `<img alt="" class="attachment-full size-full wp-image-22" decoding="async" heigh...` |
| `a7e66f489554c46e_cp1-1.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/cp1-1.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 421 no trecho: `<img alt="" class="attachment-large size-large wp-image-20" decoding="async" hei...` |
| `abc1074c4238e7f2_e2-1024x783.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e2-1024x783.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 463 no trecho: `<img alt="" class="attachment-full size-full wp-image-23" decoding="async" heigh...` |
| `b0fdf819035997e7_k2-300x112.png` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/k2-300x112.png` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 330 no trecho: `<img alt="" class="attachment-large size-large wp-image-17" decoding="async" fet...` |
| `b6308f6ffd4e8d2a_vt.webp` | `https://www.google.com/maps/vt?pb=!1m5!1m4!1i15!2i11918!3i18471!4i256!2m3!1e0!2sm!3i780544532!2m3!1e2!2sspotlit!5i1!3m13!2sen-US!3sUS!5e289!12m5!1e68!2m2!1sset!2sRoadmap!4e2!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!1e3!23i47083502!27m14!299174093m13!14m12!1m8!1m2!1y10718399135906546655!2y11839512752135877627!2s%2Fg%2F11qptkccp0!4m2!1x4071552626!2x3804343533!15sgcid%3Aplastic_surgeon!2b0!6b0!8b0&key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&token=95649` | Mapeado para resolução offline (Linha 57) |
| `b73bed2137e1c03b_e0.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e0.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 439 no trecho: `<img alt="" class="attachment-full size-full wp-image-21" decoding="async" heigh...` |
| `bf0e6b2a17965b1c_e2-300x229.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e2-300x229.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 463 no trecho: `<img alt="" class="attachment-full size-full wp-image-23" decoding="async" heigh...` |
| `c2e417b64791523b_vt.webp` | `https://www.google.com/maps/vt?pb=!1m5!1m4!1i15!2i11917!3i18471!4i256!2m3!1e0!2sm!3i780544532!2m3!1e2!2sspotlit!5i1!3m13!2sen-US!3sUS!5e289!12m5!1e68!2m2!1sset!2sRoadmap!4e2!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!1e3!23i47083502!27m14!299174093m13!14m12!1m8!1m2!1y10718399135906546655!2y11839512752135877627!2s%2Fg%2F11qptkccp0!4m2!1x4071552626!2x3804343533!15sgcid%3Aplastic_surgeon!2b0!6b0!8b0&key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&token=60700` | Mapeado para resolução offline (Linha 57) |
| `cea402a1c2a8ee9a_k1-300x112.png` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/k1-300x112.png` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 686 no trecho: `<img alt="" class="attachment-large size-large wp-image-26" decoding="async" hei...` |
| `d3a3157b0ecafc6e_e2-768x587.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e2-768x587.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 463 no trecho: `<img alt="" class="attachment-full size-full wp-image-23" decoding="async" heigh...` |
| `d3ecb8e8e107716f_e0-1024x783.jpg` | `https://drjoaoassaf.com.br/wp-content/uploads/2026/03/e0-1024x783.jpg` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 439 no trecho: `<img alt="" class="attachment-full size-full wp-image-21" decoding="async" heigh...` |
| `ee5d4b60ca116a84_vt.webp` | `https://www.google.com/maps/vt?pb=!1m5!1m4!1i15!2i11916!3i18470!4i256!2m3!1e0!2sm!3i780544532!2m3!1e2!2sspotlit!5i1!3m13!2sen-US!3sUS!5e289!12m5!1e68!2m2!1sset!2sRoadmap!4e2!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!1e3!23i47083502!27m14!299174093m13!14m12!1m8!1m2!1y10718399135906546655!2y11839512752135877627!2s%2Fg%2F11qptkccp0!4m2!1x4071552626!2x3804343533!15sgcid%3Aplastic_surgeon!2b0!6b0!8b0&key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&token=32343` | Mapeado para resolução offline (Linha 57) |

### 4.90 JSON Configuration
| Arquivo em /assets | URL Original | Utilização / Links em index.html |
| --- | --- | --- |
| `0237607dccadd849_vt.json` | `https://www.google.com/maps/vt?pb=!1m4!1m3!1i15!2i11916!3i18470!1m4!1m3!1i15!2i11916!3i18471!1m4!1m3!1i15!2i11917!3i18470!1m4!1m3!1i15!2i11917!3i18471!1m4!1m3!1i15!2i11918!3i18470!1m4!1m3!1i15!2i11918!3i18471!1m4!1m3!1i15!2i11919!3i18470!1m4!1m3!1i15!2i11919!3i18471!1m4!1m3!1i15!2i11920!3i18470!1m4!1m3!1i15!2i11920!3i18471!2m3!1e0!2sm!3i780544532!2m3!1e2!2sspotlit!5i1!3m13!2sen-US!3sUS!5e289!12m5!1e68!2m2!1sset!2sRoadmap!4e2!12m3!1e37!2m1!1ssmartmaps!4e3!12m2!5b1!6b1!27m14!299174093m13!14m12!1m8!1m2!1y10718399135906546655!2y11839512752135877627!2s%2Fg%2F11qptkccp0!4m2!1x4071552626!2x3804343533!15sgcid%3Aplastic_surgeon!2b0!6b0!8b0&key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&token=108884` | Mapeado para resolução offline (Linha 57) |
| `168c577bbbeb9757_embed.json` | `https://drjoaoassaf.com.br/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fdrjoaoassaf.com.br%2F` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 178 no trecho: `<link href="assets/json/168c577bbbeb9757_embed.json" rel="alternate" title="oEmbed (J...` |
| `7b4bc9ecebeabe5e_14.json` | `https://drjoaoassaf.com.br/wp-json/wp/v2/pages/14` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 225 no trecho: `<link href="assets/json/ef2e20f4016628ff_file.json" rel="https://api.w.org/"/><link h...` |
| `ca3d163bab055381_gen_204.json` | `https://maps.googleapis.com/maps/api/mapsjs/gen_204?csp_test=true` | Mapeado para resolução offline (Linha 57) |
| `ef2e20f4016628ff_file.json` | `https://drjoaoassaf.com.br/wp-json/` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 225 no trecho: `<link href="assets/json/ef2e20f4016628ff_file.json" rel="https://api.w.org/"/><link h...` |

### 4.98 Script (JavaScript)
| Arquivo em /assets | URL Original | Utilização / Links em index.html |
| --- | --- | --- |
| `0078eebe10ead80d_places.js` | `https://maps.googleapis.com/maps-api-v3/api/js/65/1c/places.js` | Mapeado para resolução offline (Linha 57) |
| `052c19f4719964f6_log.js` | `https://maps.googleapis.com/maps-api-v3/api/js/65/1c/log.js` | Mapeado para resolução offline (Linha 57) |
| `0b5a5914b40e518c_search.js` | `https://maps.googleapis.com/maps-api-v3/api/js/65/1c/search.js` | Mapeado para resolução offline (Linha 57) |
| `0eb0f6be05ca6315_loader.js` | `https://cdn.trustindex.io/loader.js?wp-widget` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 795 no trecho: `<script async="" data-ccm-injected="1" data-ti-widget-inited="true" data-wp-stra...` |
| `13a74d448663f3f9_nested-accordion.294d409843973.js` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/js/nested-accordion.294d40984397351fd0f5.bundle.min.js` | Mapeado para resolução offline (Linha 57) |
| `1f246c057f4a2fd3_init_embed.js` | `https://maps.gstatic.com/maps-api-v3/embed/js/65/1c/init_embed.js` | Mapeado para resolução offline (Linha 57) |
| `268cae8c2e7a7330_hello-frontend.js` | `https://drjoaoassaf.com.br/wp-content/themes/hello-elementor/assets/js/hello-frontend.js?ver=3.4.6` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 784 no trecho: `<script id="hello-theme-frontend-js" src="assets/268cae8c2e7a7330_hello-frontend...` |
| `2c7e6d34bee3736c_elements-handlers.min.js` | `https://drjoaoassaf.com.br/wp-content/plugins/pro-elements/assets/js/elements-handlers.min.js?ver=3.35.0` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 808 no trecho: `<script id="pro-elements-handlers-js" src="assets/2c7e6d34bee3736c_elements-hand...` |
| `30770e96ca66d9f1_dialog.min.js` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/lib/dialog/dialog.min.js?ver=4.9.3` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 817 no trecho: `<script src="assets/js/30770e96ca66d9f1_dialog.min.js"></script><script data-offlin...` |
| `34bbd1c367ffc7d8_jquery.sticky.min.js` | `https://drjoaoassaf.com.br/wp-content/plugins/pro-elements/assets/lib/sticky/jquery.sticky.min.js?ver=3.35.0` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 794 no trecho: `<script id="e-sticky-js" src="assets/js/34bbd1c367ffc7d8_jquery.sticky.min.js"></sc...` |
| `35b7e538abe2f782_controls.js` | `https://maps.googleapis.com/maps-api-v3/api/js/65/1c/controls.js` | Mapeado para resolução offline (Linha 57) |
| `38224b76dbe1beb2_util.js` | `https://maps.googleapis.com/maps-api-v3/api/js/65/1c/util.js` | Mapeado para resolução offline (Linha 57) |
| `4543f55b0b8bc8fe_text-editor.45609661e409413f1c.js` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/js/text-editor.45609661e409413f1cef.bundle.min.js` | Mapeado para resolução offline (Linha 57) |
| `4dddc79b1fef51de_frontend.min.js` | `https://drjoaoassaf.com.br/wp-content/plugins/pro-elements/assets/js/frontend.min.js?ver=3.35.0` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 807 no trecho: `<script id="elementor-pro-frontend-js" src="assets/4dddc79b1fef51de_frontend.min...` |
| `5274f11e6fb32ae0_jquery-migrate.min.js` | `https://drjoaoassaf.com.br/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.4.1` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 224 no trecho: `<script id="jquery-migrate-js" src="assets/5274f11e6fb32ae0_jquery-migrate.min.j...` |
| `54694c158a7f9b8f_search_impl.js` | `https://maps.googleapis.com/maps-api-v3/api/js/65/1c/search_impl.js` | Mapeado para resolução offline (Linha 57) |
| `65326f86b8e9116d_js.js` | `https://maps.googleapis.com/maps/api/js?key=DUMMY_GOOGLE_MAPS_API_KEY_REMOVED&paint_origin=&libraries=geometry,search&v=weekly&loading=async&language=en_US&callback=onApiLoad` | Mapeado para resolução offline (Linha 57) |
| `699210a5ed06e497_core.min.js` | `https://drjoaoassaf.com.br/wp-includes/js/jquery/ui/core.min.js?ver=1.13.3` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 787 no trecho: `<script id="jquery-ui-core-js" src="assets/js/699210a5ed06e497_core.min.js"></scrip...` |
| `71d6d0eda2c1cc34_main.js` | `https://maps.googleapis.com/maps-api-v3/api/js/65/1c/main.js` | Mapeado para resolução offline (Linha 57) |
| `77c0a6d635dad44b_shared-frontend-handlers.03caa.js` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/js/shared-frontend-handlers.03caa53373b56d3bab67.bundle.min.js` | Mapeado para resolução offline (Linha 57) |
| `7ec86ac58444fa5e_onion.js` | `https://maps.googleapis.com/maps-api-v3/api/js/65/1c/onion.js` | Mapeado para resolução offline (Linha 57) |
| `87cee5f49ba0d301_hooks.min.js` | `https://drjoaoassaf.com.br/wp-includes/js/dist/hooks.min.js?ver=dd5603f07f9220ed27f1` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 797 no trecho: `<script id="wp-hooks-js" src="assets/js/87cee5f49ba0d301_hooks.min.js"></script>...` |
| `a06367414e21ca69_frontend.min.js` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/js/frontend.min.js?ver=4.0.7` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 792 no trecho: `<script id="elementor-frontend-js" src="assets/js/a06367414e21ca69_frontend.min.js"...` |
| `a0fb7b5ad02ac641_nav-menu.8521a0597c50611efdc6..js` | `https://drjoaoassaf.com.br/wp-content/plugins/pro-elements/assets/js/nav-menu.8521a0597c50611efdc6.bundle.min.js` | Mapeado para resolução offline (Linha 57) |
| `aeef92f66bad0730_map.js` | `https://maps.googleapis.com/maps-api-v3/api/js/65/1c/map.js` | Mapeado para resolução offline (Linha 57) |
| `c66f47147d5fe3cc_frontend-modules.min.js` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/js/frontend-modules.min.js?ver=4.0.7` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 786 no trecho: `<script id="elementor-frontend-modules-js" src="assets/c66f47147d5fe3cc_frontend...` |
| `cb6f2d32c49d1c2b_jquery.min.js` | `https://drjoaoassaf.com.br/wp-includes/js/jquery/jquery.min.js?ver=3.7.1` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 223 no trecho: `<script id="jquery-core-js" src="assets/js/cb6f2d32c49d1c2b_jquery.min.js"></script...` |
| `d4efe709c65438ae_i18n.min.js` | `https://drjoaoassaf.com.br/wp-includes/js/dist/i18n.min.js?ver=c26c3dc7bed366793375` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 798 no trecho: `<script id="wp-i18n-js" src="assets/js/d4efe709c65438ae_i18n.min.js"></script>...` |
| `dc5eb7b7b790ae85_common.js` | `https://maps.googleapis.com/maps-api-v3/api/js/65/1c/common.js` | Mapeado para resolução offline (Linha 57) |
| `e5dc44da8489a48a_places_impl.js` | `https://maps.googleapis.com/maps-api-v3/api/js/65/1c/places_impl.js` | Mapeado para resolução offline (Linha 57) |
| `e8c5718a9e89c04a_webpack-pro.runtime.min.js` | `https://drjoaoassaf.com.br/wp-content/plugins/pro-elements/assets/js/webpack-pro.runtime.min.js?ver=3.35.0` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 796 no trecho: `<script id="elementor-pro-webpack-runtime-js" src="assets/e8c5718a9e89c04a_webpa...` |
| `ed03e4d908cc98c1_geometry.js` | `https://maps.googleapis.com/maps-api-v3/api/js/65/1c/geometry.js` | Mapeado para resolução offline (Linha 57) |
| `f9b60ae2f2938c58_jquery.smartmenus.min.js` | `https://drjoaoassaf.com.br/wp-content/plugins/pro-elements/assets/lib/smartmenus/jquery.smartmenus.min.js?ver=1.2.1` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 793 no trecho: `<script id="smartmenus-js" src="assets/js/f9b60ae2f2938c58_jquery.smartmenus.min.js...` |
| `fd9ae84b4655a6ff_webpack.runtime.min.js` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/js/webpack.runtime.min.js?ver=4.0.7` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 785 no trecho: `<script id="elementor-webpack-runtime-js" src="assets/fd9ae84b4655a6ff_webpack.r...` |

### 4.135 Stylesheet (CSS)
| Arquivo em /assets | URL Original | Utilização / Links em index.html |
| --- | --- | --- |
| `06fb30016451c923_widget-nav-menu.min.css` | `https://drjoaoassaf.com.br/wp-content/plugins/pro-elements/assets/css/widget-nav-menu.min.css?ver=3.35.0` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 210 no trecho: `<link href="assets/css/06fb30016451c923_widget-nav-menu.min.css" id="widget-nav-menu...` |
| `0a5d398672e25dc7_frontend.min.css` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/css/frontend.min.css?ver=4.0.7` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 207 no trecho: `<link href="assets/css/0a5d398672e25dc7_frontend.min.css" id="elementor-frontend-css...` |
| `13037a61480cee3d_fadeInDown.min.css` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/lib/animations/styles/fadeInDown.min.css?ver=4.0.7` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 211 no trecho: `<link href="assets/css/13037a61480cee3d_fadeInDown.min.css" id="e-animation-fadeInDo...` |
| `1b34d4c7324321e3_widget-icon-list.min.css` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/css/widget-icon-list.min.css?ver=4.0.7` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 216 no trecho: `<link href="assets/css/1b34d4c7324321e3_widget-icon-list.min.css" id="widget-icon-li...` |
| `2e3f3c9d0c58d57c_post-8.css` | `https://drjoaoassaf.com.br/wp-content/uploads/elementor/css/post-8.css?ver=1778086882` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 208 no trecho: `<link href="assets/css/2e3f3c9d0c58d57c_post-8.css" id="elementor-post-8-css" media=...` |
| `2f01a854a759c0a6_reset.css` | `https://drjoaoassaf.com.br/wp-content/themes/hello-elementor/assets/css/reset.css?ver=3.4.6` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 204 no trecho: `<link href="assets/css/2f01a854a759c0a6_reset.css" id="hello-elementor-css" media="a...` |
| `398e2425ac154b75_widget-icon-box.min.css` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/css/widget-icon-box.min.css?ver=4.0.7` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 213 no trecho: `<link href="assets/css/398e2425ac154b75_widget-icon-box.min.css" id="widget-icon-box...` |
| `3e86e49c78cd2bef_popup.min.css` | `https://drjoaoassaf.com.br/wp-content/plugins/pro-elements/assets/css/conditionals/popup.min.css?ver=3.35.0` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 783 no trecho: `<link href="assets/css/3e86e49c78cd2bef_popup.min.css" id="e-popup-css" media="all" ...` |
| `40aa8c73e7113de6_css.css` | `https://fonts.googleapis.com/css?family=Montserrat:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic&display=swap` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 222 no trecho: `<link href="assets/css/40aa8c73e7113de6_css.css" id="elementor-gf-montserrat-css" me...` |
| `45f0231564a9cfe9_post-80.css` | `https://drjoaoassaf.com.br/wp-content/uploads/elementor/css/post-80.css?ver=1779368314` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 782 no trecho: `<link href="assets/css/45f0231564a9cfe9_post-80.css" id="elementor-post-80-css" medi...` |
| `4ada91f83b55c031_widget-nested-accordion.min.css` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/css/widget-nested-accordion.min.css?ver=4.0.7` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 215 no trecho: `<link href="assets/css/4ada91f83b55c031_widget-nested-accordion.min.css" id="widget-...` |
| `5052c28c33de9956_header-footer.css` | `https://drjoaoassaf.com.br/wp-content/themes/hello-elementor/assets/css/header-footer.css?ver=3.4.6` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 206 no trecho: `<link href="assets/css/5052c28c33de9956_header-footer.css" id="hello-elementor-heade...` |
| `66830f38ccab24e9_post-14.css` | `https://drjoaoassaf.com.br/wp-content/uploads/elementor/css/post-14.css?ver=1778086882` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 218 no trecho: `<link href="assets/css/66830f38ccab24e9_post-14.css" id="elementor-post-14-css" medi...` |
| `6adb6452bc1ee069_css.css` | `https://fonts.googleapis.com/css?family=Roboto:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic&display=swap` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 219 no trecho: `<link href="assets/css/6adb6452bc1ee069_css.css" id="elementor-gf-roboto-css" media=...` |
| `6f0b2e96bd88c2d8_sticky.min.css` | `https://drjoaoassaf.com.br/wp-content/plugins/pro-elements/assets/css/modules/sticky.min.css?ver=3.35.0` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 214 no trecho: `<link href="assets/css/6f0b2e96bd88c2d8_sticky.min.css" id="e-sticky-css" media="all...` |
| `9a7cfe03ec763818_theme.css` | `https://drjoaoassaf.com.br/wp-content/themes/hello-elementor/assets/css/theme.css?ver=3.4.6` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 205 no trecho: `<link href="assets/css/9a7cfe03ec763818_theme.css" id="hello-elementor-theme-style-c...` |
| `b2394fb72dcf1d0b_css.css` | `https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Google+Sans:400,500,700|Google+Sans+Text:400,500,700&lang=en` | Mapeado para resolução offline (Linha 57) |
| `dd9c588958cd66ea_widget-google_maps.min.css` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/css/widget-google_maps.min.css?ver=4.0.7` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 217 no trecho: `<link href="assets/css/dd9c588958cd66ea_widget-google_maps.min.css" id="widget-googl...` |
| `e3e8f7f01edabf33_css.css` | `https://fonts.googleapis.com/css?family=Raleway:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic&display=swap` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 221 no trecho: `<link href="assets/css/e3e8f7f01edabf33_css.css" id="elementor-gf-raleway-css" media...` |
| `e41380127b5ea983_css.css` | `https://fonts.googleapis.com/css?family=Roboto+Slab:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic&display=swap` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 220 no trecho: `<link href="assets/css/e41380127b5ea983_css.css" id="elementor-gf-robotoslab-css" me...` |
| `eeb7e2cdafda20e5_css.css` | `https://fonts.googleapis.com/css?family=Google+Sans+Text:400&text=%E2%86%90%E2%86%92%E2%86%91%E2%86%93&lang=en` | Mapeado para resolução offline (Linha 57) |
| `f68e889145cb0e47_widget-heading.min.css` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/css/widget-heading.min.css?ver=4.0.7` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 212 no trecho: `<link href="assets/css/f68e889145cb0e47_widget-heading.min.css" id="widget-heading-c...` |
| `fb8690e594b2f9b8_widget-image.min.css` | `https://drjoaoassaf.com.br/wp-content/plugins/elementor/assets/css/widget-image.min.css?ver=4.0.7` | Mapeado para resolução offline (Linha 57)<br>Linkado na linha 209 no trecho: `<link href="assets/css/fb8690e594b2f9b8_widget-image.min.css" id="widget-image-css" ...` |

### 4.161 Web Font
| Arquivo em /assets | URL Original | Utilização / Links em index.html |
| --- | --- | --- |
| `0a44e0bb6ba5c853_KFO7CnqEu92Fr1ME7kSn66aGLdTylU.woff2` | `https://fonts.gstatic.com/s/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBHMdazQ.woff2` | Mapeado para resolução offline (Linha 57) |
| `10f1a0ef3f349790_1Ptug8zYS_SKggPNyC0IT4ttDfA.woff2` | `https://fonts.gstatic.com/s/raleway/v37/1Ptug8zYS_SKggPNyC0IT4ttDfA.woff2` | Mapeado para resolução offline (Linha 57) |
| `34da845e5e3d791f_5aUp9-KzpRiLCAt4Unrc-xIKmCU5oL.woff2` | `https://fonts.gstatic.com/s/googlesanstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmhjtjm4DZw.woff2` | Mapeado para resolução offline (Linha 57) |
| `6438d7b8ea9c7c39_JTUSjIg1_i6t8kCHKm459WlhyyTh89.woff2` | `https://fonts.gstatic.com/s/montserrat/v31/JTUSjIg1_i6t8kCHKm459WlhyyTh89Y.woff2` | Mapeado para resolução offline (Linha 57) |
| `94bae43bf209fd43_5aUu9-KzpRiLCAt4Unrc-xIKmCU5qE.woff2` | `https://fonts.gstatic.com/s/googlesanstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qEp2i0VBuxM.woff2` | Mapeado para resolução offline (Linha 57) |