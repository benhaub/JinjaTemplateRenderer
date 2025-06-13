#AI generated and slight modifications made by Ben Haubrich.

import os
from pathlib import Path

def createHeader(htmlFile, outputDir):
    # Read the HTML file as bytes
    with open(htmlFile, 'rb') as f:
        htmlBytes = f.read()
    
    # Create the header file name
    headerName = Path(htmlFile).stem + '.hpp'
    headerPath = Path(outputDir) / headerName
    
    # Create the header content
    headerContent = f"""#ifndef __WEBAPP_PAGES_{Path(htmlFile).stem.upper()}_HPP__
#define __WEBAPP_PAGES_{Path(htmlFile).stem.upper()}_HPP__
#include <cstdint>
#include <array>

namespace WebAppPages {{
    constexpr std::array<uint8_t, {len(htmlBytes)}> {Path(htmlFile).stem} = {{
        {', '.join(f'0x{b:02x}' for b in htmlBytes)}
    }};
}}

#endif // __WEBAPP_PAGES_{Path(htmlFile).stem.upper()}_HPP__
"""
    
    # Write the header file
    with open(headerPath, 'w') as f:
        f.write(headerContent)

def htmlToHeader(htmlFile, outputDirectory):
    outputDir = Path(outputDirectory)
    outputDir.mkdir(exist_ok=True)
    
    createHeader(htmlFile, outputDir)

if __name__ == '__main__':
    htmlToHeader() 
