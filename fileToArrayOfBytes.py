#AI generated and slight modifications made by Ben Haubrich.

import os
from pathlib import Path

def createHeaderWithFileAsArrayOfBytes(file, outputDir):
    with open(file, 'rb') as f:
        htmlBytes = f.read()
    
    # Create the header file name
    headerName = Path(file).stem + '.hpp'
    headerPath = Path(outputDir) / headerName
    arrayName = Path(file).stem.replace("-", "_")
    arrayName = arrayName.replace(".", "")
    
    # Create the header content
    headerContent = f"""#ifndef __WEBAPP_PAGES_{Path(file).stem.upper()}_HPP__
#define __WEBAPP_PAGES_{Path(file).stem.upper()}_HPP__
#include <cstdint>
#include <array>

namespace WebAppPages {{
    constexpr std::array<uint8_t, {len(bytes)}> {arrayName} = {{
        {', '.join(f'0x{b:02x}' for b in bytes)}
    }};
}}

#endif // __WEBAPP_PAGES_{Path(file).stem.upper()}_HPP__
"""
    
    # Write the header file
    with open(headerPath, 'w') as f:
        f.write(headerContent)

def fileToArrayOfBytes(file, outputDirectory):
    outputDir = Path(outputDirectory)
    outputDir.mkdir(exist_ok=True)
    
    createHeaderWithFileAsArrayOfBytes(file, outputDir)

if __name__ == '__main__':
    fileToArrayOfBytes() 
