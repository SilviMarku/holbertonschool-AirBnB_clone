# Web Development Basic

## HTML (HyperText Markup Language)

### What is HTML:
HTML, or HyperText Markup Language, serves as the standard markup language for creating and designing documents on the World Wide Web. It structures content using elements represented by tags, defining the meaning and purpose of the enclosed content. HTML establishes the foundation for web development by structuring elements like headings, paragraphs, links, images, and more.

### How to create an HTML page:
Creating an HTML page involves using a text editor to write HTML code. The basic structure includes a `<!DOCTYPE html>` declaration, an `<html>` element with `<head>` and `<body>` sections. The head holds metadata and links to external resources, while the body contains the actual content. Example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is my first HTML page.</p>
</body>
</html>
```

### What is a markup language:
A markup language is a system for annotating text to indicate desired structure and presentation. HTML, designed for web documents, uses tags to define elements within content.

### What is the DOM (Document Object Model):
The DOM is a programming interface representing the structure of a document as a tree of objects. It allows dynamic manipulation of content, structure, and style using languages like JavaScript.

### What is an element/tag:
An HTML element, or tag, is a building block consisting of an opening tag, content, and a closing tag. For instance, `<p>` is an opening tag for a paragraph element, and `</p>` is its closing tag.

### What is an attribute:
Attributes provide additional information about HTML elements. They modify behavior or appearance and are included in the opening tag as name/value pairs. Example:

```html
<img src="image.jpg" alt="A descriptive text">
```

### How does the browser load a webpage:
The browser requests the HTML file from the server, receives content, parses HTML to construct the DOM, fetches external resources, and renders the webpage.

## CSS (Cascading Style Sheets)

### What is CSS:
CSS, or Cascading Style Sheets, is a style sheet language describing the presentation and formatting of HTML documents. It controls layout, appearance, and styling of elements.

### How to add style to an element:
CSS rules consist of a selector targeting an element and a declaration block specifying styles. Example:

```css
p {
    color: red;
}
```

### What is a class:
A class is a way to apply styles or behavior to multiple elements with a common identifier, defined using the `class` attribute.

```html
<p class="highlight">This paragraph has a special style.</p>
```

### What is a selector:
A selector in CSS is a pattern defining which elements will be targeted by a style rule based on type, class, ID, attributes, etc.

### How to compute CSS Specificity Value:
CSS specificity measures how specific a selector is, influencing precedence when rules conflict. It is calculated using components like inline styles, IDs, classes/attributes, and elements.

### What are Box properties in CSS:
CSS box properties determine dimensions and spacing of elements, including width, height, margin, padding, and border.

## Additional CSS Concepts

### How Grid Systems Work (with Floats):
Grid systems organize content into rows and columns for structured layouts. Floats, traditionally used, are now complemented by modern layout techniques like Flexbox and CSS Grid.

### The Difference Between Icons Webfonts and SVG Icons:
Icons webfonts use custom font files containing icon glyphs, styled with CSS. SVG icons use XML-based vector images, providing flexibility in size and color.

### The Difference Between Pseudo-classes and Pseudo-elements:
Pseudo-classes target states of elements (e.g., `:hover`), while pseudo-elements target specific parts of elements (e.g., `::before`).

### How to Make Background Gradients:
CSS gradients provide smooth color transitions for element backgrounds using `linear-gradient` or `radial-gradient` functions.

### How to Animate Elements in CSS:
CSS animations gradually change an element's style over time using keyframes to define intermediate stages.

### How to Transform (2D, 3D) Elements:
CSS transforms modify an element's appearance, allowing translation, rotation, scaling, etc., using the `transform` property.

### What Vendor Prefixes Are:
Vendor prefixes (e.g., `-webkit-`, `-moz-`) enable experimental or proprietary features during implementation, ensuring compatibility during development.
