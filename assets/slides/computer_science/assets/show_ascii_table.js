const ascii032 = "NUL SOH STX ETX EOT ENQ ACK BEL BS TAB LF VT FF CR SO SI DLE DC1 DC2 DC3 DC4 NAK SYN ETB CAN EM SUB ESC FS GS RS US SPACE".split(' ');

function showAsciiTable(id) {  
  const asciiTable = document.getElementById(id);
  for (var code = 0; code < 128; code++) {
    const params = colorChar(code);
    
    let c = document.createElement("div");    
    c.innerHTML = `<strong>${params.data}</strong>`;
    c.className = params.class;
    
    let s = document.createElement("span");    
    s.className ='asciisup';
    s.innerHTML = `${code}<br/>#${code.toString(16)}`;
    c.appendChild(s);    
    asciiTable.appendChild(c);
  }
}
showAsciiTable("asciiTable");

function colorChar(code) {
  
  if (code <= 32)    
    return {class:'ctrl', data: ascii032[code]};
    
  if (code == 127)    
    return { class: "ctrl", data: "DEL" };
      
  var chr = String.fromCharCode(code);  
  if (chr >= '0' && chr <= '9') 
    return { class: "digit", data: chr };
  else if ( (chr >= "A" && chr <= "Z") || (chr >= "a" && chr <= "z") ) 
    return { class: "char", data: chr };
  else
    return { class: "", data: chr };
}