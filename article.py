import scribus
import xml.etree.ElementTree as ET

def create_text_frame(x, y, width, height, text):
    """
    Create a text frame at position (x, y) with specified width and height, and set the text content.
    """
    frame = scribus.createText(x, y, width, height)
    scribus.setText(text, frame)
    return frame

def import_articles_from_xml(news_file):
    """
    Import news articles from the provided XML file and add them to the Scribus document.
    """
    tree = ET.parse(news_file)
    root = tree.getroot()
    
    # Define dimensions and positions
    x, y = 10, 10
    width, height = 200, 50
    spacing = 10

    for article in root.findall('article'):
        title = article.find('title').text
        description = article.find('description').text

        # Create title text frame
        create_text_frame(x, y, width, height, title)
        y += height + spacing

        # Create description text frame
        create_text_frame(x, y, width, height, description)
        y += height + spacing

def main():
    if not scribus.haveDoc():
        scribus.messageBox('Error', 'No document open', scribus.ICON_WARNING, scribus.BUTTON_OK)
        return

    # Path to the XML file
    news_file = scribus.fileDialog('Select XML file', filter='XML Files (*.xml)')
    
    if not news_file:
        scribus.messageBox('Error', 'No XML file selected', scribus.ICON_WARNING, scribus.BUTTON_OK)
        return

    import_articles_from_xml(news_file)

if __name__ == "__main__":
    main()
