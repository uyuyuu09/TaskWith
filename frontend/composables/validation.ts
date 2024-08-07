export function validateFormData(email: string, password: string): { cur_email: boolean, cur_pass: boolean } {
    const emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    const cur_email = emailRegex.test(email);
    const cur_pass = password.length >= 8;
    return { cur_email, cur_pass };
}
