## Notis: 
- Upgift 1 - klar
  - Veckouppgift1.dia - Koppling mellan klasserna (ritat med DIA)
  - Veckouppgift1.pdf - README i pdf
  - Veckouppgift1.png - export av dia-file till png
- Upgift 2 - ej klar eller pushat än (troligen klar ikväll)

# Activity Management System

Detta projekt beskriver ett system för att hantera personer, aktiviteter, registreringar och uthyrning av utrustning.

## Innehåll

- [Person](#person)
- [Activity](#activity)
- [Register](#register)
- [Equipment_rent](#equipment_rent)
- [Systemöversikt](#systemöversikt)

---

# Person

```text
+--------------------------------------+
|                Person                |
+--------------------------------------+
| - User                               |
| - First_name                         |
| - Last_name                          |
| - Email                              |
| - Phone                              |
| - Status                             |
+--------------------------------------+
| + Add_User()                         |
| + Get_User_Info()                    |
| + Update_User_info()                 |
| + Delete_User()                      |
| + Set_Status()                       |
+--------------------------------------+
```

Klassen **Person** representerar en person som vill delta i en aktivitet.

## Attribut

Exempel på värden:

| Attribut | Exempel |
|---|---|
| `First_name` | `"Kalle"` |
| `Last_name` | `"Anka"` |
| `Email` | `"kalle.anka@anke.borg"` |
| `Phone` | `"123456789"` |
| `Status` | `true` |

## Metoder

- **`Add_User()`** – skapar ett användarkonto genom att registrera nödvändig information om användaren.
- **`Get_User_Info()`** – hämtar relevant information om en användare och returnerar ett `Person`-objekt.
- **`Update_User_info()`** – uppdaterar användarens information genom att skicka in de attribut som ska ändras.
- **`Delete_User()`** – söker efter användarens konto och tar bort det.
- **`Set_Status()`** – söker upp användaren och ändrar kontots status. En användare kan exempelvis ha statusen **aktiv** eller **inaktiv**.

---

# Activity

```text
+--------------------------------------+
|               Activity               |
+--------------------------------------+
| - Activity                           |
| - Date                               |
| - LeadUser                           |
| - Status                             |
+--------------------------------------+
| + Add_Activity()                     |
| + Update_Activity()                  |
+--------------------------------------+
```

Klassen **Activity** representerar en aktivitet eller ett evenemang i systemet.

## Attribut

Exempel på värden:

| Attribut | Exempel |
|---|---|
| `Activity` | `"Vandring"` |
| `Date` | `2026-09-01` |
| `LeadUser` | `"kalle.anka@anke.borg"` |
| `Status` | `true` |

## Metoder

- **`Add_Activity()`** – skapar en ny aktivitet. Vid skapandet anges bland annat aktivitetens startdatum och slutdatum. En ansvarig ledare ska också anges för aktiviteten.
- **`Update_Activity()`** – uppdaterar relevanta attribut för en befintlig aktivitet, exempelvis datum, ledare eller status.

---

# Register

```text
+--------------------------------------+
|               Register               |
+--------------------------------------+
| - Reg_date                           |
| - Payment                            |
| - User                               |
| - Activity                           |
| - Status                             |
+--------------------------------------+
| + Add_reg()                          |
| + GetAll()                           |
| + Get_User()                         |
| + Get_Activity()                     |
| + Get_Payment()                      |
| + SetNew_Status()                    |
+--------------------------------------+
```

Klassen **Register** används för att hantera registreringar till aktiviteter. Den kopplar ihop en **Person** med en **Activity**.

## Attribut

Ett registreringsobjekt kan till exempel innehålla:

| Attribut | Exempel |
|---|---|
| `Reg_date` | `2026-08-22` |
| `Payment` | `200 kr` |
| `User` | `"kalle.anka@anke.borg"` |
| `Activity` | `"Vandring"` |
| `Status` | `true` |

## Relation

```text
+---------+
| Person  |
+----+----+
     |
     | registrerar sig
     v
+----------+
| Register |
+----+-----+
     |
     | till
     v
+-----------+
| Activity  |
+-----------+
```

Det innebär att en person kan registrera sig till en aktivitet.

Klassen `Register` fungerar som en länk mellan personen och aktiviteten och innehåller information om exempelvis:

- Registreringsdatum
- Betalning
- Användare
- Aktivitet
- Status

## Metoder

- **`Add_reg()`** – skapar en ny registrering till en aktivitet.
- **`GetAll()`** – hämtar alla registreringar.
- **`Get_User()`** – hämtar information om användaren som är kopplad till registreringen.
- **`Get_Activity()`** – hämtar information om aktiviteten som registreringen gäller.
- **`Get_Payment()`** – hämtar betalningsinformationen för registreringen.
- **`SetNew_Status()`** – ändrar statusen för registreringen.

---

# Equipment_rent

```text
+--------------------------------------+
|           Equipment_rent             |
+--------------------------------------+
| - Rent_Date                          |
| - Return_Date                        |
| - User                               |
| - Comment                            |
| - Status                             |
+--------------------------------------+
| + Reg_Rent()                         |
| + Change_Rent_Status()               |
| + Check_Rent_Status()                |
+--------------------------------------+
```

Klassen **Equipment_rent** används för att hantera uthyrning av utrustning till användare.

## Attribut

Ett uthyrningsobjekt kan till exempel innehålla:

| Attribut | Exempel |
|---|---|
| `User` | `"kalle.anka@anke.borg"` |
| `Equipment` | `"Vandringskäpp"` |
| `Rent_Date` | `2026-08-22` |
| `Return_Date` | `2026-08-25` |
| `Status` | `true` |

> **Observera:** `Equipment` används i exemplet ovan men finns inte med som attribut i det ursprungliga klassdiagrammet.

## Metoder

- **`Reg_Rent()`** – registrerar en ny uthyrning.
- **`Change_Rent_Status()`** – ändrar statusen för en uthyrning, exempelvis när utrustningen lämnas tillbaka.
- **`Check_Rent_Status()`** – kontrollerar statusen för uthyrningen.

## Relation

```text
+---------+
| Person  |
+----+----+
     |
     | hyr
     v
+----------------+
| Equipment_rent |
+-------+--------+
        |
        | gäller
        v
+-------------+
| Equipment   |
+-------------+
```

Det innebär att en person kan hyra utrustning.

Klassen `Equipment_rent` håller reda på själva uthyrningen, exempelvis:

- Vem som hyr utrustningen
- När utrustningen hämtades
- När utrustningen ska lämnas tillbaka
- Kommentarer
- Uthyrningens status

---

# Systemöversikt

Systemets huvudsakliga relationer kan sammanfattas enligt följande:

```text
                 +---------+
                 | Person  |
                 +----+----+
                      |
             +--------+--------+
             |                 |
       registrerar sig        hyr
             |                 |
             v                 v
       +----------+     +----------------+
       | Register |     | Equipment_rent |
       +----+-----+     +-------+--------+
            |                   |
            | till              | gäller
            v                   v
       +-----------+      +-------------+
       | Activity  |      | Equipment   |
       +-----------+      +-------------+
```

## Sammanfattning

Systemet består av personer som kan:

1. Skapa och hantera användarkonton.
2. Registrera sig till aktiviteter.
3. Delta i aktiviteter.
4. Hyra utrustning.

De olika klasserna har följande huvudsakliga ansvar:

| Klass | Ansvar |
|---|---|
| `Person` | Hantera användare och deras information |
| `Activity` | Hantera aktiviteter och evenemang |
| `Register` | Hantera registreringar mellan personer och aktiviteter |
| `Equipment_rent` | Hantera uthyrning av utrustning |

`Register` används för att hantera kopplingen mellan personer och aktiviteter, medan `Equipment_rent` används för att hantera uthyrningen av utrustning.
