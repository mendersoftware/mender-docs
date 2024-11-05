flowchart TD
    %% Main node with boxed global settings
    A(["**Service Provider**<br><div style='border: 1px solid #000; padding: 5px; margin-top: 5px;'>***Device limit: 100***</div><div style='border: 1px solid #000; padding: 5px; margin-top: 5px;'>***Global security policy***</div><br>👤 SP Admin"])

    %% Child nodes with boxed device limits and user sections
    A --> B(["**Child 1**<br><div style='border: 1px solid #000; padding: 5px; margin-top: 5px;'>***Device limit: 20***</div><div style='border: 1px solid #000; padding: 5px; margin-top: 5px; text-align: left;'>👤 Admin 1<br>👤 User A<br>👤 User B</div>"])
    A --> C(["**Child 2**<br><div style='border: 1px solid #000; padding: 5px; margin-top: 5px;'>***Device limit: 40***</div><div style='border: 1px solid #000; padding: 5px; margin-top: 5px; text-align: left;'>👤 Admin 2<br>👤 User A</div>"])
    A --> D(["**Child 3**<br><div style='border: 1px solid #000; padding: 5px; margin-top: 5px;'>***Device limit: 40***</div><div style='border: 1px solid #000; padding: 5px; margin-top: 5px; text-align: left;'>👤 Admin 3<br>👤 User B</div>"])